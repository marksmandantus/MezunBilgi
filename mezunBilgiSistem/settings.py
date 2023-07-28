from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_vmul+h+@0u32s1tq8yb-kjs92de6m-uh27z&j50%b_(gc%j4d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'crispy_bootstrap4',
    'crispy_forms',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'base.apps.BaseConfig',
    'job.apps.JobConfig',
    'rest_framework',
    'django_extensions',
    ]

# crispy template pack
CRISPY_TEMPLATE_PACK = 'bootstrap4'

AUTH_USER_MODEL = 'base.Person'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mezunBilgiSistem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates",
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

WSGI_APPLICATION = 'mezunBilgiSistem.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'graduate',
        'USER': 'root',
        'PASSWORD': '2001',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]


# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ANYMAIL = {
    'MAILJET_API_KEY': '8ba7bc20a39ef0a5625899239144c04a',  
    'MAILJET_SECRET_KEY': '6c8c4321b6373548d5b02983ded123c1',
}

#SMTP CONFIGURATION

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASS")
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")

#JAZZMIN CONFIGURATION

JAZZMIN_SETTINGS = {
    "site_icon": None,
    "welcome_sign": "Mezun Bilgi Admin Paneli",
}

JAZZMIN_UI_TWEAKS = {
    "theme": "darkly",
}

#MEDIA CONFIGURATION    

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'



