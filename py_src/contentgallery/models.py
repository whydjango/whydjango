'''
Created on Sep 11, 2010

@author: jonas
'''
from cms.models.pluginmodel import CMSPlugin
from contentgallery.widgets import LazyHTMLField
from django.db import models
from django.utils.html import strip_tags
from django.utils.translation import ugettext_lazy as _
from tinymce.models import HTMLField


class ContentGalleryPlugin(CMSPlugin):
    title = models.CharField(_('title'), max_length=255, blank=True, default='')
    description = HTMLField(blank=True, default='')
    
    def __unicode__(self):
        return self.title
    
    
class Slide(models.Model):
    gallery = models.ForeignKey(ContentGalleryPlugin, related_name='slides')
    order = models.PositiveIntegerField(default=0)
    title = models.CharField(_('title'), max_length=255, default='')
    description = LazyHTMLField(default='')
    
    class Meta:
        ordering = ['-order']
    
    def __unicode__(self):
        return '%s...' % strip_tags(self.description)[:30] 