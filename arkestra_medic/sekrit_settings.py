DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'richard',                      # Or path to database file if using sqlite3.
        'USER': 'richard',                      # Not used with sqlite3.
        'PASSWORD': 'funct1on4nd',                  # Not used with sqlite3.
        'HOST': '/tmp/mysql.sock',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
#     }
# }

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake-live-2013-jan-30'
    }
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
#         'LOCATION': '/var/tmp/django_cache-live-2012-feb-27',
#     }
# }



# Make this unique, and don't share it with anybody.
SECRET_KEY = 'n!xrr^hhh&rm$#vcq7eg=p-n-p2wiccc*5^vocgitt5ez&##ra'

# ------------------------ authentication

import ldap
from django_auth_ldap.config import LDAPSearch

AUTH_LDAP_SERVER_URI = "ldap://zldap1.cf.ac.uk"
AUTH_LDAP_BIND_DN = ""
AUTH_LDAP_BIND_PASSWORD = ""
AUTH_LDAP_USER_SEARCH = LDAPSearch("t=faraway",
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}

# This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True
# LOGIN_REDIRECT_URL = "/admin/"
# LOGIN_URL = "/admin/"
# old LDAP stuff
"""
LDAP_SERVER_URI = 'ldap://ldap.cf.ac.uk' 
LDAP_SEARCHDN = 't=faraway' 
LDAP_SCOPE = ldap.SCOPE_SUBTREE 
LDAP_SEARCH_FILTER = 'cn=%s' 
LDAP_UPDATE_FIELDS = True 
LDAP_BIND_ATTRIBUTE = ''
LDAP_FIRST_NAME = 'givenName'
LDAP_LAST_NAME = 'sn'
LDAP_EMAIL = 'mail'
"""
 
# ------------------------ Django Celery
try:
    import djcelery
    djcelery.setup_loader()

    BROKER_HOST = "localhost"
    BROKER_PORT = 5672
    BROKER_USER = "guest"
    BROKER_PASSWORD = "guest"
    BROKER_VHOST = "/"
except ImportError:
    pass
