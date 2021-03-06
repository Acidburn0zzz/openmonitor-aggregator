#!/usr/bin/env python
# -*- coding: utf-8 -*-
##
## Author: Adriano Monteiro Marques <adriano@umitproject.org>
## Author: Diogo Pinheiro <diogormpinheiro@gmail.com>
##
## Copyright (C) 2011 S2S Network Consultoria e Tecnologia da Informacao LTDA
##
## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU Affero General Public License as
## published by the Free Software Foundation, either version 3 of the
## License, or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Affero General Public License for more details.
##
## You should have received a copy of the GNU Affero General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.
##

import os
from os.path import dirname
from os.path import abspath
from os.path import join


import djcelery
djcelery.setup_loader()

import import_deps


AGG_DIR =  dirname(abspath(__file__))

DATABASES = {'default': {'ENGINE': 'django.db.backends.mysql',
                           'NAME':'openmonitor',
                           'USER':'root',
                           'PASSWORD':'',
                           'HOST':'localhost',
                           'PORT':3306,
                           'TEST_NAME':'openmonitor_test'},
             #"mysql": {'ENGINE': 'mysql',
             #          'NAME':'openmonitor',
             #          'USER':'root',
             #          'PASSWORD':'root',
             #          'HOST':'localhost',
             #          'PORT':3306,
             #          'TEST_NAME':'openmonitor_test'}
             }

#DATABASE_ROUTERS = ['gui.dbrouters.GeoIPRouter']

#AUTOLOAD_SITECONF = 'indexes'

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

DEBUG = True
TEMPLATE_DEBUG = DEBUG
CACHE_MIDDLEWARE_SECONDS = 30

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# PISTON SETTINGS
PISTON_DISPLAY_ERRORS = DEBUG
PISTON_EMAIL_ERRORS = "adriano@umitproject.org"
PISTON_STREAM_OUTPUT = DEBUG

ENVIRONMENT = os.environ.get('SERVER_SOFTWARE', '')
PRODUCTION = False
TEST = True


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    #'django.contrib.sites',
    'autoload',
    #'djangologging',
    #'protobuf',
    'piston',
    #'messages',
    'agents',
    'geoip',
    'api',
    'gui',
    'reports',
    'suggestions',
    'events',
    'versions',
    'icm_tests',
    'twitter',
    'notificationsystem',
    'registration',
    'filetransfers',
    'ajax_select',
    'djcelery',
    'mediagenerator',
)

MIDDLEWARE_CLASSES = (
    'mediagenerator.middleware.MediaMiddleware',
    
    # This loads the index definitions, so it has to come first
    'autoload.middleware.AutoloadMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware', # CACHE
    #'django.middleware.csrf.CsrfViewMiddleware', # CSRF

    'django.middleware.common.CommonMiddleware', # CACHE
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'djangologging.middleware.LoggingMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'gui.context_processors.basic',
)

FIXTURE_DIRS = (AGG_DIR,)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
#TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ADMIN_MEDIA_ROOT = os.path.join(AGG_DIR, 'static/')
ADMIN_MEDIA_PREFIX = 'http://localhost:9000/static/'
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

#TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)
#Remove comment in the following line for v2 design
TEMPLATE_DIRS = (join(AGG_DIR, 'templates', 'v2'),)

ROOT_URLCONF = 'urls'

ROOT_MEDIA_FILTERS = {
    'js': 'mediagenerator.filters.yuicompressor.YUICompressor',
    'css': 'mediagenerator.filters.yuicompressor.YUICompressor',
}

YUICOMPRESSOR_PATH = join(AGG_DIR, 'yuicompressor-2.4.7.jar')

MEDIA_BUNDLES = (
     ('main.css',
         'css/jquery-ui.css',
         ),
     ('main-old.css',
         'css/main.css',
         'css/jquery-ui.css',
         ),
     ('main.js',
         {'filter': 'mediagenerator.filters.media_url.MediaURL'},
         #'js/jquery.js',
         'bs/assets/js/jquery.js', #Use bootstrap's jQuery
         'js/jquery-ui.js',
         'js/jquery-scrollbarwidth.js',
         'js/date.format.js',
         'js/markerclusterer.js',
         'js/common.js',
         'js/realtimebox.js',
         'js/map.js',
         'js/events.js',),
     ('bootstrap.css',
         'bs/assets/css/bootstrap-responsive.css',
         'bs/assets/css/bootstrap.css',
          ),
     ('bootstrap.js',
         {'filter': 'mediagenerator.filters.media_url.MediaURL'},
          'bs/assets/js/bootstrap-transition.js',
          'bs/assets/js/bootstrap-alert.js',
          'bs/assets/js/bootstrap-modal.js',
          'bs/assets/js/bootstrap-dropdown.js',
          'bs/assets/js/bootstrap-scrollspy.js',
          'bs/assets/js/bootstrap-tab.js',
          'bs/assets/js/bootstrap-tooltip.js',
          'bs/assets/js/bootstrap-popover.js',
          'bs/assets/js/bootstrap-button.js',
          'bs/assets/js/bootstrap-collapse.js',
          'bs/assets/js/bootstrap-carousel.js',
          'bs/assets/js/bootstrap-typeahead.js',),
)

MEDIA_DEV_MODE = DEBUG
DEV_MEDIA_URL = '/devmedia/'
PRODUCTION_MEDIA_URL = '/media/'

NOTIFICATION_SENDER = "notification@openmonitor.org"
NOTIFICATION_TO = "notification@openmonitor.org"
NOTIFICATION_REPLY_TO = "notification@openmonitor.org"

GLOBAL_MEDIA_DIRS = (join(AGG_DIR, 'media'), join(AGG_DIR, 'static'))

INTERNAL_IPS = ('127.0.0.1', 'localhost',)
LOGGING_OUTPUT_ENABLED = True


# add support to user profile
AUTH_PROFILE_MODULE = 'users.UserProfile'
ACCOUNT_ACTIVATION_DAYS = 30
LOGIN_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
#'django.core.mail.backends.console.EmailBackend'

EMAIL_HOST = 'mail'
EMAIL_HOST_USER = 'notification@openmonitor.org'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25
EMAIL_USE_TLS = False

#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'gmailusername@gmail.com'
#EMAIL_HOST_PASSWORD = 'xxxxxxx'
#EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'notification@openmonitor.org'
SERVER_EMAIL = 'notification@openmonitor.org'

USE_I18N = True

#Don't need to use folowing in development
#On deployment, Make sure you uncomment it and set to appropriate site key
#SITE_ID = u'' # Empty by default because Nonrel IDs are not integer

##################
# RESPONSE COUNTS
MAX_NETLIST_RESPONSE = 10
MAX_AGENTSLIST_RESPONSE = 5

#########################
# File Transfer settings
PREPARE_UPLOAD_BACKEND = 'filetransfers.backends.delegate.prepare_upload'
#PRIVATE_PREPARE_UPLOAD_BACKEND = 'djangoappengine.storage.prepare_upload'
#PUBLIC_PREPARE_UPLOAD_BACKEND = 'djangoappengine.storage.prepare_upload'
#SERVE_FILE_BACKEND = 'djangoappengine.storage.serve_file'
PUBLIC_DOWNLOAD_URL_BACKEND = 'filetransfers.backends.base_url.public_download_url'
PUBLIC_DOWNLOADS_URL_BASE = '/data/'


# aggregator private key
RSAKEY_MOD = 93740173714873692520486809225128030132198461438147249362129501889664779512410440220785650833428588898698591424963196756217514115251721698086685512592960422731696162410024157767288910468830028582731342024445624992243984053669314926468760439060317134193339836267660799899385710848833751883032635625332235630111
RSAKEY_EXP = 65537
RSAKEY_D = 62297015822781158796363618856389920569720490554603739852574703225696321267124285722204224123764419501867928817657919519054848555406464849450959012702348251941541095546410973524267691136995700233299378960173993986706088589136001011922024584878399897228054794884245267290619407261307654480907250669720474301281
RSAKEY_P = 7757705817565141349021648120631369992682141789699152399326127816192467211564791533199816990028647490792876630757010309393888042701542789312864387282715209
RSAKEY_Q = 12083491681603271568173938267128976608289124671971871656030565887109349091047806314688865045109296709421488821701923256321238599753290254378297945671005479
RSAKEY_U = 4807166779721366881723532650380832638823203637550840979310831953962905310688603113539132663918756964730460591047978835536521726443169772132990407509799218


RSA_KEYSIZE = 1024


######################
# AJAX_SELECT OPTIONS

AJAX_SELECT_BOOTSTRAP = True
AJAX_SELECT_INLINES = 'inline'

#######################
# AJAX LOOKUP CHANNELS
AJAX_LOOKUP_CHANNELS = {
    'location': ('geoip.lookups', 'LocationLookup'),
}

#####################
# CELERY OPTIONS
BROKER_URL = 'redis://localhost:6379/0'
CELERY_DISABLE_RATE_LIMITS = True
CELERY_RESULT_BACKEND = 'database'
CELERY_RESULT_DBURI = "mysql://root@localhost/openmonitor"
CELERY_ALWAYS_EAGER = False
CELERY_REDIRECT_STDOUTS_LEVEL = "DEBUG"
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}  # 1 hour.
