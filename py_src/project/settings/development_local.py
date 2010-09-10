from project.settings.development import *

IS_DEV_SERVER = True
CACHE_BACKEND = 'locmem://'


# DATABASE SETTINGS
DATABASES = {
   'default': {
       'ENGINE': 'sqlite3',
       'NAME': 'db.sqlite',
   },
}
