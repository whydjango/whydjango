from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from contentgallery import models
from django.contrib import admin


class SlideInline(admin.StackedInline):
    model = models.Slide
    template = 'admin/content_gallery_inline.html'


class ContentGalleryPlugin(CMSPluginBase):
    model = models.ContentGalleryPlugin
    name = _("Content Gallery")
    render_template = "plugins/content_gallery.html"
    text_enabled = False
    admin_preview = False
    inlines = [
        SlideInline,
    ]
    
    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context
    
plugin_pool.register_plugin(ContentGalleryPlugin)