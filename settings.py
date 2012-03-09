# -*- coding: utf-8 -*-

"""
A sample of kay settings.

:Copyright: (c) 2009 Accense Technology, Inc. 
                     Takashi Matsuo <tmatsuo@candit.jp>,
                     All rights reserved.
:license: BSD, see LICENSE for more details.
"""
import os
import sys
import logging
# library path setting
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_LIB_DIR = os.path.join(PROJECT_DIR, 'lib')
sys.path.insert(0, os.path.join(PROJECT_LIB_DIR, 'reportlab.zip'))
sys.path.insert(0, os.path.join(PROJECT_LIB_DIR, 'html5lib.zip'))
sys.path.insert(0, os.path.join(PROJECT_LIB_DIR, 'rl_addons.zip'))
sys.path.insert(0, os.path.join(PROJECT_LIB_DIR, 'xhtml2pdf.zip'))

# static dir
STATIC_DIR = os.path.join(PROJECT_DIR, 'static')
STATIC_IMAGE_DIR = os.path.join(STATIC_DIR, 'images')
STATIC_FONTS_DIR = os.path.join(STATIC_DIR, 'fonts')

DEFAULT_TIMEZONE = 'Asia/Tokyo'
DEBUG = True
PROFILE = False
SECRET_KEY = 'ReplaceItWithSecretString'
SESSION_PREFIX = 'gaesess:'
COOKIE_AGE = 1209600 # 2 weeks
COOKIE_NAME = 'KAY_SESSION'
FLASH_COOKIE_NAME = 'FLASH_COOKIE_NAME'

ADD_APP_PREFIX_TO_KIND = True

ADMINS = (
)

TEMPLATE_DIRS = (
    'templates',
)

USE_I18N = True
DEFAULT_LANG = 'ja'

INSTALLED_APPS = (
    'welcome',
)

APP_MOUNT_POINTS = {
    'welcome': '/',
}


# Middleware
MIDDLEWARE_CLASSES = (
    'kay.sessions.middleware.SessionMiddleware',
    'kay.utils.flash.FlashMiddleware',
)

# You can remove following settings if unnecessary.
CONTEXT_PROCESSORS = (
    'kay.context_processors.request',
    'kay.context_processors.url_functions',
    'kay.context_processors.media_url',
)

