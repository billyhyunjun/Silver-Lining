"""
Django settings for SilverLining project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path
from . import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR 설정
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.SETTING_KEY
OPEN_API_KEY = config.OPEN_API_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ### install_app ###
    'rest_framework',  # REST framework 설치
    'modeltranslation',  # 다국어 지원을 위한 모듈
    'django_celery_beat',  # 셀러리를 위한 기능
    'django_celery_results',  # 셀러리를 위한 기능
    ### custom_app ###
    'accounts',  # 사용자 계정 관리 앱
    'menus',  # 메뉴 관리 앱
    'orders',  # 주문 관리 앱
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",  # 다국어 지원을 위한 미들웨어
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SilverLining.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # 템플릿 디렉터리 설정
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

WSGI_APPLICATION = 'SilverLining.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',  # Docker Compose 파일에서 설정한 데이터베이스 이름과 동일하게 설정
        'USER': 'myuser',  # Docker Compose 파일에서 설정한 사용자 이름과 동일하게 설정
        'PASSWORD': 'mypassword',  # Docker Compose 파일에서 설정한 비밀번호와 동일하게 설정
        'HOST': 'db',  # Docker Compose 파일에서 설정한 PostgreSQL 서비스의 이름과 동일하게 설정
        'PORT': '5432',
    }
}



CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}


AUTH_USER_MODEL = "accounts.User"  # 사용자 모델 지정

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ko'  # 기본 언어 설정
LANGUAGE_COOKIE_NAME = 'django_language'  # 언어 쿠키 이름

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ko'  # 다국어 모델의 기본 언어 설정

TIME_ZONE = 'UTC'  # 기본 타임존 설정

USE_TZ = True
USE_I18N = True
USE_L10N = True

LOCALE_PATHS = [
    BASE_DIR / 'locale',  # 번역 파일의 경로 설정
]

LANGUAGES = [
    ('ko', 'Korean'),  # 한국어
    ('en', 'English'),  # 영어
    ('ja', 'Japanese'),  # 일본어
    ('zh-hans', 'Chinese'),  # 중국어
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_ALWAYS_EAGER = True
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Seoul'

