#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHORS = 'John Bachman, Carlos Lopez, Alex Lubbock, Jeremy Muhlich'
SITENAME = 'PySB'
SITESUBTITLE = 'Systems biology modeling in Python'
SITEURL = ''
SITELOGO = '/images/pysb-swirl.png'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = 'themes/pelican-blueidea'

STATIC_PATHS = ['images', 'extra/']
EXTRA_PATH_METADATA = {}
for f in os.listdir('content/extra/'):
    EXTRA_PATH_METADATA['extra/'+f] = {'path':f}

MENUITEMS=[('Home', '/'),
           ('News', '/category/news.html'),
           ('Support', '/support.html')]
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False
