from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from custom_plugins.models import FeatureImagePlugin as FeatureImagePluginModel

class FeatureImagePlugin(CMSPluginBase):
    model = FeatureImagePluginModel
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