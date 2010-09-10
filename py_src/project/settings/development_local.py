from project.settings.development import *

IS_DEV_SERVER = True
CACHE_BACKEND = 'db://dbcache'


# DATABASE SETTINGS
DATABASES = {
   'default': {
       'ENGINE': 'sqlite3',
       'NAME': 'db.sqlite',
   },
}
