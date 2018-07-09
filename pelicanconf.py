#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Nicolae Cleju'
SITENAME = 'Dr. Nicolae Cleju'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Bucharest'

DEFAULT_LANG = 'ro'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
DEFAULT_DATE = 'fs'

#THEME = 'blueidea'

PLUGIN_PATHS = ['~//pelican-plugins']
PLUGINS = ['assets', 'sitemap', 'gravatar']
