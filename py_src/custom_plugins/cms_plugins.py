from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from custom_plugins import models

class FeatureImagePlugin(CMSPluginBase):
    model = models.FeatureImagePlugin
    name = _("Feature Image")
    render_template = "plugins/feature_image.html"
    text_enabled = False
    admin_preview = False
    
    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context
    
plugin_pool.register_plugin(FeatureImagePlugin)


class GridPlugin(CMSPluginBase):
    model = models.GridPlugin
    name = _("Grid")
    render_template = "plugins/grid.html"
    text_enabled = False
    admin_preview = False
    
    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context
    
plugin_pool.register_plugin(GridPlugin)