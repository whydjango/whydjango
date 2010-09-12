from django.conf import settings
from django.forms.util import flatatt
from django.template.defaultfilters import escape
from django.utils.encoding import smart_unicode
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE, get_language_config
from django.utils import simplejson
import tinymce


class LazyTinyMCEWidget(TinyMCE):
    """
    This creates a tiny mce textarea, but does not initialize it like the base class does, so that it's not broken
    when it comes back from hiding :)
    """
    def render(self, name, value, attrs=None):
        if value is None: value = ''
        value = smart_unicode(value)
        final_attrs = self.build_attrs(attrs)
        final_attrs['name'] = name
        assert 'id' in final_attrs, "TinyMCE widget attributes must contain 'id'"

        mce_config = tinymce.settings.DEFAULT_CONFIG
        mce_config.update(get_language_config(self.content_language))
        if tinymce.settings.USE_FILEBROWSER:
            mce_config['file_browser_callback'] = "djangoFileBrowser"
        mce_config.update(self.mce_attrs)
        mce_config['mode'] = 'exact'
        mce_config['elements'] = final_attrs['id']
        mce_config['strict_loading_mode'] = 1
        mce_json = simplejson.dumps(mce_config)

        html = [u'<textarea%s>%s</textarea>' % (flatatt(final_attrs), escape(value))]
        if tinymce.settings.USE_COMPRESSOR:
            compressor_config = {
                'plugins': mce_config.get('plugins', ''),
                'themes': mce_config.get('theme', 'advanced'),
                'languages': mce_config.get('language', ''),
                'diskcache': True,
                'debug': False,
            }
            compressor_json = simplejson.dumps(compressor_config)
            
            # Now the trick - instead of ouputting <javascript> tags and initializing when they are rendered, 
            # let's simply put the json string in a hidden div and fetch the info / initialize when the view
            # actually displays them :)
            
            #html.append(u'<script type="text/javascript">tinyMCE_GZ.init(%s)</script>' % compressor_json)
            html.append(u'<div style="visibility:hidden" class="uninitialized-tiny-field" id="hidden_div_%s">%s</div>' % (final_attrs['id'], compressor_json))
        
        #html.append(u'<script type="text/javascript">tinyMCE.init(%s)</script>' % mce_json)
        html.append(r'<div style="visibility:hidden" class="uninitialized-tiny-field" id="hidden_div_%s">%s</div>' % (final_attrs['id'], mce_json))    

        return mark_safe(u'\n'.join(html))
    

class LazyHTMLField(HTMLField):
    """
    A large string field for HTML content. It uses the TinyMCE widget in
    forms, and this one should pass the "minimal" settings to the actual rendering.
    """
    def formfield(self, **kwargs):
        defaults = {'widget': LazyTinyMCEWidget}
        return super(LazyHTMLField, self).formfield(**defaults)