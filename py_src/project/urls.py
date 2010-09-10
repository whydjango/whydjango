from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

handler404 = "project.views.page_not_found"
handler500 = "project.views.server_error"

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
    # CMS *MUST* BE LAST!
    (r'', include('cms.urls')),
)

if settings.IS_DEV_SERVER:
    if 'appmedia' in settings.INSTALLED_APPS:
        urlpatterns = patterns('',
            (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
        ) + urlpatterns
    else:
        urlpatterns = patterns('',
            (r'^' + settings.MEDIA_URL.lstrip('/') + '(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + urlpatterns
    if settings.IS_HTTP_SERVER:
        urlpatterns += patterns('',
            (r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT + '../', 'show_indexes': True}),
        )