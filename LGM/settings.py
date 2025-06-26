from pathlib import Path
import os
import os
import dj_database_url


# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = '15s%-i*vvg4l*dwbk@rm((5spl@eo=2ze1=7p+!b2$7k+j=#(i'

# DEBUG = False

# ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['localhost', '127.0.0.1']
import os  # Make sure this is at the top of the file

SECRET_KEY = os.environ.get("SECRET_KEY", "15s%-i*vvg4l*dwbk@rm((5spl@eo=2ze1=7p+!b2$7k+j=#(i")

DEBUG = os.environ.get("DEBUG", "True") == "True"

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")



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

# MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

MIDDLEWARE = [
    
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
#     'default': {
       
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': os.environ['LGM'],
#         'USER': os.environ['root'],
#         'PASSWORD': os.environ['root'],
#         'HOST': os.environ['localhost'],
#         'PORT': os.environ.get('MYSQLPORT', '3306'),
#     }
# }

DATABASES = {
    'default': dj_database_url.parse(os.environ.get("mysql://root:LrTXuFVzHfmdikOlVPBOWdSZnEZwZlfW@trolley.proxy.rlwy.net:26218/railway"))
}

AUTH_USER_MODEL = 'core.CustomUser'


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
# STATIC_URL = 'static/'
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT = BASE_DIR / 'staticfiles'


# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
