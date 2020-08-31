#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date

import sys
import os


AUTHOR = u'Apache Central Services'
SITENAME = u'Welcome to the Apache Software Foundation'
SITEURL = ''
CURRENTYEAR = date.today().year

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'
SITEURL = 'https://www.apache.org'
STATIC_PATHS = ['pages/.htaccess']
# Save pages using full directory preservation
PATH_METADATA= '.*?(pages/)?(?P<path_no_ext>.*?)\.[a-z]*$'
PAGE_SAVE_AS= '{path_no_ext}.html'
PAGE_URL= '{path_no_ext}.html'
#IGNORE_FILES = []
READERS = {'htaccess': None}
#SLUGIFY_SOURCE = 'basename'
#PAGE_PATHS = ['content']

# Standard behavior:

ARTICLE_SAVE_AS = 'news/{slug}.html'
ARTICLE_URL = 'news/{slug}.html'

# Sort news by date, descending, latest article first
ARTICLE_ORDER_BY = 'reversed-date'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# TOC Generator
PLUGIN_PATHS = ['./theme/plugins']
PLUGINS = ['toc']
TOC_HEADERS = r"h[1-6]"

DEFAULT_PAGINATION = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
