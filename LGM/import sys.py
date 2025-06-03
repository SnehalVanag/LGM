import sys
import os
import types
import importlib
import pathlib
import pytest
from . import settings

# test_settings.py


# Import the settings module using a relative import

def test_base_dir_is_path():
    assert isinstance(settings.BASE_DIR, pathlib.Path)

def test_secret_key_is_nonempty_string():
    assert isinstance(settings.SECRET_KEY, str)
    assert settings.SECRET_KEY != ""

def test_debug_is_boolean():
    assert isinstance(settings.DEBUG, bool)

def test_allowed_hosts_is_list():
    assert isinstance(settings.ALLOWED_HOSTS, list)

def test_root_urlconf():
    assert settings.ROOT_URLCONF == "LGM.urls"

def test_wsgi_application():
    assert settings.WSGI_APPLICATION == "LGM.wsgi.application"

def test_installed_apps():
    required = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'core'
    ]
    for app in required:
        assert app in settings.INSTALLED_APPS

def test_templates_dirs():
    assert isinstance(settings.TEMPLATES, list)
    assert 'DIRS' in settings.TEMPLATES[0]
    assert settings.TEMPLATES[0]['DIRS'][0].name == 'templates'

def test_databases_config():
    assert 'default' in settings.DATABASES
    db = settings.DATABASES['default']
    assert isinstance(db, dict)
    assert 'ENGINE' in db
    assert 'NAME' in db
    assert 'USER' in db
    assert 'PASSWORD' in db
    assert 'HOST' in db
    assert 'PORT' in db

def test_static_url_and_root():
    assert isinstance(settings.STATIC_URL, str)
    assert settings.STATIC_URL
    assert isinstance(settings.STATIC_ROOT, str)
    assert settings.STATIC_ROOT

def test_default_auto_field():
    assert settings.DEFAULT_AUTO_FIELD == 'django.db.models.BigAutoField'