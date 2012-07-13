# Django settings for arkestra_medic project.

from sekrit_settings import *

import os
gettext = lambda s: s 

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': '',                      # Or path to database file if using sqlite3.
#       'USER': '',                      # Not used with sqlite3.
#       'PASSWORD': '',                  # Not used with sqlite3.
#       'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#       'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#   }
#}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
# USE_TZ = True

BASE_PATH = os.path.normpath(os.path.dirname(__file__))

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = BASE_PATH+'/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_PATH, "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
# SECRET_KEY = '7g8^r53fr1xsen(2qzolj-z1k%(1#+8w(5e(84zh8btw*-*z6n'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    'django.core.context_processors.static',
    'django.contrib.messages.context_processors.messages',
    "cms.context_processors.media",
    'sekizai.context_processors.sekizai',
    "arkestra_utilities.context_processors.arkestra_templates",
)

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'cms.middleware.multilingual.MultilingualURLMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',    
)

ROOT_URLCONF = 'arkestra_medic.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'arkestra_medic.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_PATH+'/templates/',
)

# ------------------------ authentication

AUTHENTICATION_BACKENDS = (
    #'django.contrib.auth.backends.RemoteUserBackend',
    #'auth.ldapauth.LDAPBackend',
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_PROFILE_MODULE = 'contacts_and_people.Person'

ENABLE_CONTACTS_AND_PEOPLE_AUTH_ADMIN_INTEGRATION=True


# ------------------------ Django CMS

CMS_SOFTROOT = True
CMS_PERMISSION = True
CMS_SEO_FIELDS = True
CMS_HIDE_UNTRANSLATED = False

# this is only here because I don't know how to make other apps find it otherwise, and they rely on it.
CMS_MEDIA_URL = STATIC_URL + 'cms/'

CMS_TEMPLATES = (
    #('cardiff/arkestra.html', gettext('Arkestra')),
    # ('institute.html', gettext('Institute of Mediaeval Medicine')),
    ('cardiff/medic.html', gettext('School of Medicine')),
    ('cardiff/medic/cngg.html', gettext('CNGG')),
    ('cardiff/medic/fhwales.html', gettext('FH Wales')),
    ('cardiff/medic/c21.html', gettext('C21')),
    ('clinicalresearchfacility.html', gettext('Clinical Research Facility')),
    ('mothersofafrica.html', gettext('Mothers of Africa')),
)

CMS_PAGE_FLAGS = (
    ('no_local_menu', 'Hide local menu') ,
    ('no_horizontal_menu', 'No horizontal menu') ,
    ('no_page_title', "Don't display page title") ,
    )

CMS_PLACEHOLDER_CONF = {                        
    'body': {
        "plugins": (
            'SemanticTextPlugin', 
            'CMSVacanciesPlugin', 
            'CMSNewsAndEventsPlugin', 
            'SnippetPlugin', 
            'LinksPlugin', 
            'CMSPublicationsPlugin', 
            'ImagePlugin', 
            'ImageSetPublisher',
            'FilerImagePlugin', 
            'EntityDirectoryPluginPublisher', 
            'CarouselPluginPublisher',
            'FocusOnPluginPublisher',
            'VideoPluginPublisher',
            ),
        "extra_context": {            
            "width":"749",
            },
        "name": gettext("body"),
    },
}

CMS_LANGUAGES = (
('en', gettext('English')),
('it', gettext('Italiano')),
('cy', gettext('Cymraeg')),
)

# CMS_MODERATOR = False
INSTALLED_APPS = (

     # Django CMS applications
    
    'arkestra_utilities',
    'cms',
    'menus',
    'cms.plugins.text',
    'cms.plugins.snippet',
    # 'menupreview',
    'sekizai',
    # 'djcelery',     # will need to be enabled for celery processing
    
    # Arkestra applications
    
    'contacts_and_people',
    'vacancies_and_studentships',
    'news_and_events',
    'links',
    'arkestra_utilities.widgets.combobox',
    'arkestra_image_plugin',
    'video',
    'housekeeping',
    'publications',
    'symplectic',
    
    # other applications
    
    'polymorphic',
    'semanticeditor',
    'mptt',
    'easy_thumbnails',
    'typogrify',
    'filer',    
    'widgetry',  
    'south',         
    # 'adminsortable',
    
    
    # core Django applications

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
# FILER_ENABLE_PERMISSIONS = True
from arkestra_settings import *
# import pdb; pdb.set_trace()
