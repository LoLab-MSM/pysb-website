#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHORS = 'John Bachman, Carlos Lopez, Alex Lubbock, Jeremy Muhlich'
SITENAME = 'PySB'
SITESUBTITLE = 'Systems biology modeling in Python'
SITEURL = 'https://lolab-vu.github.io/pysb-website'
SITELOGO = '/images/pysb-swirl.png'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

THEME = 'themes/pelican-blueidea'

STATIC_PATHS = ['images']

MENUITEMS=[('Home', '/'),
           ('Support', '/support.html')]
DISPLAY_PAGES_ON_MENU = False
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False
