#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Odyssey'
SITENAME= 'Odyssey'
SITEURL = ''
PATH = 'content'

TIMEZONE = 'Asia/Singapore'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
        ('SPMS Official Page for the Odyssey Programme', 'https://spms.ntu.edu.sg/Programmes/Undergrads/Odyssey/Pages/Home.aspx'),
        ('Telegram Announcements', 'https://t.me/odysseyprogramme'),
        ('Instagram Page', 'https://instagram.com/odysseyprogramme'),
        ('Email us', '#'),
)
        # ('Whatsapp Announcement Group', '#'),
"""
('Archival for Talks this semester', '#'),
('Ongoing Projects', '#'),
('SPMS Official Page for the Odyssey Programme', 'https://spms.ntu.edu.sg/Programmes/Undergrads/Odyssey/Pages/Home.aspx'),
('OI', '#'),)
"""

# Social widget
SOCIAL = (
        ('Telegram', '#'),
        ('Instagram Page', '#'),
        ('Another social link', '#'),)
        #('Whatsapp Announcement Group', '#'),

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


THEME = 'themes/bricks/'

STATIC_PATHS = [
    'images',
    'extra',  # this
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},  # and this
}

LOAD_CONTENT_CACHE = False
