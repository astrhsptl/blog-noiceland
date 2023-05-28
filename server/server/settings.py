import os
import socket
import environ

from pathlib import Path

# Environ settings
# https://django-environ.readthedocs.io/en/latest/
env = environ.Env()
environ.Env.read_env('.env')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-vakb02ds@g(izf(x-3pf@_+_98ypnequy*9h3_7!37@tx+9w6(' #os.getenv('SECRET_KEY')
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(env('DEBUG')))

ALLOWED_HOSTS = ['0.0.0.0', '127.0.0.1', 'alexander.kizimenko.fvds.ru']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # second part
    'allauth', 
    'allauth.account',
    'allauth.socialaccount',
    'drf_yasg',
    'whitenoise',
    'corsheaders',
    'crispy_forms',
    'rest_framework',
    'debug_toolbar',

    # third part
    'authsystem.apps.AuthsystemConfig',
    'pages.apps.PagesConfig',
    'APIpoints.apps.ApipointsConfig'

]

MIDDLEWARE = [
    # 'django.middleware.cache.UpdateCacheMiddleware',# - cache middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # cors headers
    'django.middleware.common.CommonMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # whitenoise
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',# - cache middleware
]

ROOT_URLCONF = 'server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': env('DB_NAME'),
#         'USER': env('DB_USER'),
#         'PASSWORD': env('DB_PASSWORD'),
#         'HOST': env('DB_HOST'),
#         'PORT': int( env('DB_PORT') ),
#     }
# }

# Rest Framework Settings
# https://www.django-rest-framework.org

REST_FRAMEWORK = {
    # 'DEFAULT_RENDERER_CLASSES': [
    #     'rest_framework.renderers.JSONRenderer',
    # ],
    # 'DEFAULT_PARSER_CLASSES': [
    #     'rest_framework.parsers.JSONParser',
    # ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'server.jwt.JWTAuthClass'
    ]
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(STATIC_ROOT, 'pages/'),
]

# Media
# https://docs.djangoproject.com/en/4.1/topics/files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Email settings
# https://docs.djangoproject.com/en/4.1/topics/email/

DEFAULT_FROM_EMAIL = env('EMAIL')
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_HOST_USER = env('EMAIL')
EMAIL_HOST_PASSWORD = env('EMAIL_PASSWORD')
EMAIL_PORT = int(env('EMAIL_PORT'))
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

# Celery options
# https://docs.celeryq.dev/en/stable/

# REDIS_HOST = 'redis'
REDIS_HOST = 'redis'
REDIS_PORT = str(6379)

CELERY_BROKER_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
CELERY_TRANSPORT_OPTIONS = {'visibilitytimeout': 3600}
CELERY_RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# All-Auth configutation
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SITE_ID = 1

ACCOUNT_FORMS = {
    "login": "allauth.account.forms.LoginForm",
    "add_email": "allauth.account.forms.AddEmailForm",
    "change_password": "allauth.account.forms.ChangePasswordForm",
    "set_password": "allauth.account.forms.SetPasswordForm",
    "reset_password": "allauth.account.forms.ResetPasswordForm",
    "reset_password_from_key": "allauth.account.forms.ResetPasswordKeyForm",
    "disconnect": "allauth.socialaccount.forms.DisconnectForm",

    "signup": "authsystem.forms.CustomSignupForm",
}

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'account_login'
ACCOUNT_LOGOUT_REDIRECT = 'home'
ACCOUNT_MAX_EMAIL_ADDRESSES = 1
ACCOUNT_EMAIL_VERIFICATION = 'none'

AUTHENTICATION_BACKENDS = (
'django.contrib.auth.backends.ModelBackend',
'allauth.account.auth_backends.AuthenticationBackend',
)

AUTH_USER_MODEL = 'authsystem.User' 


ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_CONFIRMATION_HMAC = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_EMAIL_REQUIRED = True

# Crispy forms settings
# https://django-crispy-forms.readthedocs.io/en/latest/

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Cors Headers Settings
# https://github.com/adamchainz/django-cors-headers

CORS_ALLOW_ALL_ORIGINS = True 

# WhiteNoise settings
# https://github.com/evansd/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Debug Toolbar Settings
# https://django-debug-toolbar.readthedocs.io/en/latest/index.html

hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]

### DAJNGO SECURITY
# https://docs.djangoproject.com/en/4.1/topics/security/

# XFrame options
# https://docs.djangoproject.com/en/4.1/ref/clickjacking/

# X_FRAME_OPTIONS = 'SAMEORIGIN'

# CSRF settings
# https://docs.djangoproject.com/en/4.1/ref/csrf/
 
CSRF_COOKIE_SECURE = False

# XSS settings
# https://docs.djangoproject.com/en/4.1/topics/security/#cross-site-scripting-xss-protection

SECURE_BROWSER_XSS_FILTER = False

# SSL& HSTS settings
# https://docs.djangoproject.com/en/4.1/topics/security/#ssl-https

SECURE_SSL_REDIRECT = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_PRELOAD = False

# Session settings
# https://docs.djangoproject.com/en/4.1/topics/http/sessions/#settings

SESSION_COOKIE_SECURE = False

# Secure content settings

SECURE_CONTENT_TYPE_NOSNIFF = False