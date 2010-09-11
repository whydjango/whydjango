from cms.models import CMSPlugin
from django.db import models
from django.db.models.signals import post_save
from filer.fields.image import FilerImageField

class FeatureImagePlugin(CMSPlugin):
    image = FilerImageField()
    

class Grid(models.Model):
    title = models.CharField(max_length=255)
    
    def __unicode__(self):
        return self.title
    
    def get_rows(self):
        return GridRow.objects.filter(grid=self).select_related('cells', 'cells__column')


class GridRow(models.Model):
    grid = models.ForeignKey(Grid, related_name='rows')
    order = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['-order']
    
    def __unicode__(self):
        return self.name


class GridColumn(models.Model):
    grid = models.ForeignKey(Grid, related_name='columns')
    order = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['-order']
    
    def __unicode__(self):
        return self.name


class GridCell(models.Model):
    row = models.ForeignKey(GridRow, related_name='cells', editable=False)
    column = models.ForeignKey(GridColumn, related_name='cells', editable=False)
    text = models.CharField(max_length=255, blank=True)
    
    class Meta:
        unique_together = [('row', 'column'),]
    
    def __unicode__(self):
        prefix = '[%s/%s]' % (self.row.name, self.column.name)
        return '%s %s' % (prefix, self.text)


class GridPlugin(CMSPlugin):
    grid = models.ForeignKey(Grid)

    def __unicode__(self):
        return self.cached_grid.title
    
    def get_rows(self):
        return self.cached_grid.get_rows()
    
    def get_columns(self):
        return self.cached_grid.columns.all()
    
    @property
    def cached_grid(self):
        if not hasattr(self, '__cached_grid'):
            self.__cached_grid = Grid.objects.filter(pk=self.grid_id).select_related()[0]
        return self.__cached_grid
            

def auto_add_rows(instance, created, **kwargs):
    """
    Generates empty cells for new columns
    """
    if not created:
        return
    for row in instance.grid.rows.all():
        GridCell.objects.get_or_create(row=row, column=instance)
post_save.connect(auto_add_rows, sender=GridColumn)

def auto_add_columns(instance, created, **kwargs):
    """
    Generates empty cells for new rows
    """
    if not created:
        return
    for column in instance.grid.columns.all():
        GridCell.objects.get_or_create(row=instance, column=column)
post_save.connect(auto_add_columns, sender=GridRow)