from custom_plugins.models import GridColumn, GridCell, GridRow, Grid
from django.contrib import admin

class GridCellInline(admin.StackedInline):
    model = GridCell
    extra = 0
    can_delete = False
    max_num = 0


class GridColumnAdmin(admin.ModelAdmin):
    inlines = [
        GridCellInline,
    ]
    

class GridRowAdmin(admin.ModelAdmin):
    inlines = [
        GridCellInline,
    ]
    

admin.site.register(GridColumn, GridColumnAdmin)
admin.site.register(GridRow, GridRowAdmin)
admin.site.register(Grid)