# CMS SETTINGS
gettext = lambda s: s
CMS_TEMPLATES = (
    ('tpl_master.html', gettext('master template')),
    ('tpl_col-two.html', gettext('row two-columns')),
    ('tpl_col-three.html', gettext('row three-columns')),
    ('tpl_home.html', gettext('home template')),
)

'''
CMS_PLACEHOLDER_CONF = {
    'col_content': {
        'plugins': (',),
        'name': gettext("column content"),
        'extra_context': {"submenucolumn":False},
    },

    'col_sidebar': {
        'plugins': (,),
        'name': gettext('column sidebar'),
        'extra_context': {"submenucolumn":False},
    },

    'col_aside': {
        'plugins': (,),
        'name': gettext('column aside'),
        'extra_context': {"submenucolumn":False},
    },
}
'''

CMS_PAGE_MEDIA_PATH = 'uploads/cms_page_media/'
CMS_SOFTROOT = True
CMS_FLAT_URLS = False
CMS_REDIRECTS = True
CMS_SEO_FIELDS = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_USE_TINYMCE = True
CMS_PERMISSION = True
CMS_MODERATOR = False # DO NOT CHANGE THIS!

CMS_SHOW_START_DATE = True
CMS_SHOW_END_DATE = True

# PLUGIN SETTINGS
FILER_UPLOAD_ROOT = 'private/filer'

THUMBNAIL_BASEDIR = 'tmp'
THUMBNAIL_QUALITY = 70
THUMBNAIL_PROCESSORS = (
    'filer.utils.sorl_filters.scale_and_crop',
    # Default processors
    'sorl.thumbnail.processors.colorspace',
    'sorl.thumbnail.processors.autocrop',
    #'sorl.thumbnail.processors.scale_and_crop',
    'sorl.thumbnail.processors.filters',
)

# PLUGIN TEASER SETTINGS
CMSPLUGIN_FILER_TEASER_STYLE_CHOICES = (
    # ('plugin_teaser_picleft','Bild Links'),
)

# PLUGIN SIMPLE GALLERY SETTINGS
CMSPLUGIN_SIMPLE_GALLERY_STYLE_CHOICES = (
    # ('thumbnailview','Thumbnail Galerie'),
)

IMAGE_ASPECT_RATIO_CHOICES = (
    (1, '1:1'),
    (1.33333, '4:3'),
    (1.77777, '16:9'),
    (2.33333, '21:9'),
)

# PLUGIN VIDEO SETTINGS
VIDEO_PLUGIN_ENABLE_ADVANCED_SETTINGS = False # disable color settings etc

# TINYMCE SETTINGS
TINYMCE_BASE_URL = '/media/tiny_mce/'
TINYMCE_JS_URL = TINYMCE_BASE_URL + 'tiny_mce.js'
TINYMCE_DEFAULT_CONFIG = dict(
    theme = "advanced",
    skin = "o2k7",
    plugins = "advimage,advlink,table,searchreplace,contextmenu,paste,save,autosave,template,bramus_cssextras",#,spellchecker
    visual = True,
    # Appearance
    width = "640",
    height = "300",
    theme_advanced_buttons1 = "formatselect,styleselect,separator,removeformat,template,separator,code,cleanup",
    theme_advanced_buttons2 = "pastetext,pasteword,separator,bold,italic,separator,bullist,numlist,separator,link,unlink,anchor,separator,tablecontrols",#"search,replace,cleanup,separator,formatselect,separator,help",
    theme_advanced_buttons3 = "",
    theme_advanced_blockformats = "p,h2,h3,h4,h5,h6",
    theme_advanced_toolbar_location = "top",
    theme_advanced_toolbar_align = "left",
    theme_advanced_statusbar_location = "bottom",
    theme_advanced_resizing = False,
    # Styles
    paste_remove_styles = True,
    paste_remove_spans = True,
    content_css = '/media/css/base.css',
    show_styles_menu = False,
    # (X)HTML
    convert_urls = False,
    fix_nesting = True,
    cleanup_on_startup = True,
    cleanup = True,
    forced_root_block = "p",
    extended_valid_elements = 'a[class|name|href|title|onclick],img[class|src|alt=image|id|title|onmouseover|onmouseout],p[id|style|dir|class],span[class|style],br[class|clear|id|style|title]',
    object_resizing = False,
    invalid_elements = "font,strike,u",
    convert_fonts_to_spans = False,
    removeformat_selector = 'b,strong,em,i,span,ins',
    gecko_spellcheck = False,
    style_formats = [                     
        {'title':'Text styles'},
        {'title':'Text left', 'selector':'p,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes':'align-left'},  
        {'title':'Text right', 'selector':'p,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes':'align-right'},
        {'title':'Text center', 'selector':'p,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes':'align-center'},
       
        {'title':'Object styles'},
        {'title':'Float left', 'selector':'p,h2,h3,h4,h5,h6,div,ul,ol,table,img', 'classes':'left'},  
        {'title':'Float right', 'selector':'p,h2,h3,h4,h5,h6,div,ul,ol,table,img', 'classes':'right'},        
        {'title':'Clear', 'selector':'p,h2,h3,h4,h5,h6,div,ul,ol,table,img', 'classes':'clear'}
    ],
    template_templates = []
)
# spellchecking plugin has to be installed manually
TINYMCE_SPELLCHECKER = False
TINYMCE_FILEBROWSER = False