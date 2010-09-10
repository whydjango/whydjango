# -*- coding: utf-8 -*-
from base_i18n import *
from base_cms import *

import os

DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = False

TEMPLATE_DEBUG = DEBUG
IS_DEV_SERVER = False
IS_HTTP_SERVER = False
PREPEND_WWW = False
FORCE_SCRIPT_NAME = ''

USE_ETAGS = False

INTERNAL_IPS = ('127.0.0.1',)

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Europe/Zurich'


SITE_ID = 1

USE_I18N = True

USE_L10N = True

# "../" because we are in a package
PROJECT_DIR = os.path.abspath( os.path.join(os.path.dirname(__file__),'../') )

MEDIA_ROOT = PROJECT_DIR + '/media/'

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = '8XBzdfuIFwn5sds6D1Rsk1QCXLP99Kdm0wVIB3cFb14WsXQfM0'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
  # 'django.middleware.gzip.GZipMiddleware', # gzip conflict with video (swf plugin)
  # 'cms.middleware.media.PlaceholderMediaMiddleware',
    'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'siteinfo.middleware.login_required.RequireLoginMiddleware',
  # 'project.safe_gzip_middleware.SafeGZipMiddleware',
)

ROOT_URLCONF = 'project.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',

	# standard plugins
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.snippet',
    'cms.plugins.text',
    'cms.plugins.twitter',
    'cms.plugins.video',
    'cmsplugin_filer_file',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',

    # standard apps
    'appmedia',
    'cms',
    'filer',
    'menus',
    'mptt',
    'sekizai',
    'sorl.thumbnail',
    'south',
    'tinymce',
    'uni_form',

    # custom apps
    'project',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    "cms.context_processors.media",
    "siteinfo.context_processors.siteinfo",
    "sekizai.context_processors.sekizai",
)

# PUT REAL FROM EMAIL HERE
# DEFAULT_FROM_EMAIL = 'noreply@project.ch'
SERVER_EMAIL = 'django@%s' % os.uname()[1]

# DEFAULT DATE SETTINGS
DATE_FORMAT = 'd.m.Y'
DATETIME_FORMAT = 'd.m.Y H:i'
TIME_FORMAT = 'H:i'
YEAR_MONTH_FORMAT = 'F Y'
MONTH_DAY_FORMAT = 'j. F'
