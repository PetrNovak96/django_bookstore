"""
Django settings for bookstore_project project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '*c=%_@f3m*r&&o2azah-=_8-ksy-4z7-ciq(-tw-&p$cx(d*@v'
SECRET_KEY = os.environ.get('SECRET_KEY') # new

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = int(os.environ.get('DEBUG', default=0)) # new

ALLOWED_HOSTS = ['.herokuapp.com', 'localhost', '127.0.0.1']

ENVIRONMENT = os.environ.get('ENVIRONMENT', default='development')

print("environment",ENVIRONMENT)
# production
if ENVIRONMENT == 'production':
    SECURE_BROWSER_XSS_FILTER = True # new
    X_FRAME_OPTIONS = 'DENY'  # new (clickjacking)
    SECURE_SSL_REDIRECT = True  # new
    SECURE_HSTS_SECONDS = 3600  # new
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # new
    SECURE_HSTS_PRELOAD = True  # new
    SECURE_CONTENT_TYPE_NOSNIFF = True  # new
    SESSION_COOKIE_SECURE = True  # new
    CSRF_COOKIE_SECURE = True  # new

# Application definition

INSTALLED_APPS = [

    # Local
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'books.apps.BooksConfig',
    'orders.apps.OrdersConfig',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', # new

    # Third-party
    'crispy_forms', # new
    'allauth', # new
    'allauth.account', # new
    'debug_toolbar', # new
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware', # new
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware', # new
    'django.middleware.cache.FetchFromCacheMiddleware', # new
]

ROOT_URLCONF = 'bookstore_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # new
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookstore_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'postgres',
        'PORT': 5432
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),] # new
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # new
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

AUTH_USER_MODEL = 'users.CustomUser' # new

LOGIN_REDIRECT_URL = 'home' # new

LOGOUT_REDIRECT_URL = 'home' # new

CRISPY_TEMPLATE_PACK = 'bootstrap4' # new

# django-allauth config
# https://learndjango.com/tutorials/django-allauth-tutorial
SITE_ID = 1 # new
ACCOUNT_LOGOUT_REDIRECT = 'home' # new
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend', # new
)
ACCOUNT_SESSION_REMEMBER = True # new
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False # new
ACCOUNT_USERNAME_REQUIRED = False # new
ACCOUNT_AUTHENTICATION_METHOD = 'email' # new
ACCOUNT_EMAIL_REQUIRED = True # new
ACCOUNT_UNIQUE_EMAIL = True # new

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # new
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' # new
DEFAULT_FROM_EMAIL = 'admin@djangobookstore.com' # new
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# media
MEDIA_URL = '/media/' # new
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # new

# Stripe
STRIPE_TEST_PUBLISHABLE_KEY=os.environ.get('STRIPE_TEST_PUBLISHABLE_KEY')
STRIPE_TEST_SECRET_KEY=os.environ.get('STRIPE_TEST_SECRET_KEY')

# django-debug-toolbar
import socket
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 604800
CACHE_MIDDLEWARE_KEY_PREFIX = ''