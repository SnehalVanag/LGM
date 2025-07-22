from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv
import pymysql
pymysql.install_as_MySQLdb()
import socket




BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ON_PYTHONANYWHERE = socket.gethostname().endswith(".pythonanywhere.com")

if ON_PYTHONANYWHERE:
    DATABASES = {
        'default': dj_database_url.config(
            default='mysql://peakprosys:Snehal@123@peakprosys.mysql.pythonanywhere-services.com:3306/peakprosys$dblgm'
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


#  DATABASES = {
#     'default': dj_database_url.config(
#         default='mysql://peakprosys:Snehal@123@peakprosys.mysql.pythonanywhere-services.com:3306/peakprosys$dblgm'
#     )
# }
# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR/".eVar",".env"))

SECRET_KEY = '15s%-i*vvg4l*dwbk@rm((5spl@eo=2ze1=7p+!b2$7k+j=#(i'
DEBUG = True
ALLOWED_HOSTS = ['localhost', '127.0.0.1']


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'product_images'

# ✅ Add this line to point to your project-level urls.py
ROOT_URLCONF = 'LGM.urls'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',  # Your custom app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core' / 'templates'],  # Custom templates directory
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

WSGI_APPLICATION = 'LGM.wsgi.application'

# DATABASES = {
#     'default':dj_database_url.config(
#         default = "mysql://root:root@localhost:3306/LGM"+os.path.join(BASE_DIR,"db.sqllite")
#     )
# }
# DATABASES = {
#     'default': dj_database_url.config(
#         default='mysql://peakprosys:Snehal@123@peakprosys.mysql.pythonanywhere-services.com:3306/peakprosys$dblgm'
#     )
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'LGM',
#         'USER': 'root',
#         'PASSWORD': 'root',
#         'HOST': 'localhost',
#         'PORT': '3306',
#     }
# }
# AUTH_USER_MODEL = 'core.CustomUser'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'snehalvanage57@gmail.com'  # Replace with your Gmail
# EMAIL_HOST_PASSWORD = 'vycg jerl yfcq iknf'  # Replace with your app password



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'lgtmlgtm18@gmail.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'skoe bktu ktyh tbqu'  # Replace with your app password
# Custom user model (if applicable)
AUTH_USER_MODEL = 'core.CustomUser'

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

# Static files
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
