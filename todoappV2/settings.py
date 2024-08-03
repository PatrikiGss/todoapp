# Importações e definições de caminho
from pathlib import Path
import os
import sys
from decouple import config, Csv # type: ignore

BASE_DIR = Path(__file__).resolve().parent.parent

APP_DIR = os.path.join(BASE_DIR, 'apps')
sys.path.insert(0, APP_DIR)

# Verificando as variáveis de ambiente
secret_key = config('SECRET_KEY')
debug_mode = config('DEBUG', default=False, cast=bool)

# Variáveis sensíveis e configuração de depuração
SECRET_KEY = secret_key
DEBUG = debug_mode
ALLOWED_HOSTS = []

# Aplicações Django e de terceiros
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

THIRD_APPS = []  # Apps de terceiros podem ser adicionadas aqui

# Aplicações do projeto
PROJECT_APPS = [
    'core.apps.CoreConfig',
    'taskmanager.apps.TaskmanagerConfig',
    'tasks.apps.TasksConfig',
    'accounts.apps.AccountsConfig',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'todoappV2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'todoappV2.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

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

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'