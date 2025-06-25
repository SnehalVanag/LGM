from pathlib import Path
import os


from pathlib import Path
from pathlib import Path # Path might already be there
from dotenv import load_dotenv

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".eVar", ".env"))
import pymysql
pymysql.install_as_MySQLdb()



STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*#x=h$@73w2jk$1cae@%ee8y69=@ro+!n8pb&_(+q%-+=sz6d8'  # Replace with your own key in production

# ... rest of your settings
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG')
ALLOWED_HOSTS = ["127.0.0.1",'localhost']  # Add your production domain here
ALLOWED_HOSTS  +=os.environ.get('ALLOWED_HOSTS', '').split()  # Allow multiple hosts from environment variable




SECRET_KEY = '15s%-i*vvg4l*dwbk@rm((5spl@eo=2ze1=7p+!b2$7k+j=#(i'

DEBUG = True

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['localhost', '127.0.0.1']


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'product_images'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Now BASE_DIR is defined

# Optional for media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


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
    'whitenoise.middleware.WhiteNoiseMiddleware',
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




AUTH_USER_MODEL = 'core.CustomUser'
WSGI_APPLICATION = 'LGM.wsgi.application'

# DATABASES = {
#    'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': "LGM",
#         'USER': "snehalvanage123",
#         'PASSWORD': "root#123@12",
#         'HOST': "snehalvanage123.mysql.pythonanywhere-services.com",
#         'PORT': "3306"
# }

# }


DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'snehalvanage123$lgm',  # This is the full name, with username prefix
            'USER': 'snehalvanage123',             # Your PythonAnywhere DB username
            'PASSWORD': 'root#123@12',        # Set this when you created the DB
            'HOST': 'snehalvanage123.mysql.pythonanywhere-services.com',
            'PORT': '3306',
    }
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



# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
