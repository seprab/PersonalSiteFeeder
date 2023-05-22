#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'SepraB'
SITENAME = "SepraB's"
SITEURL = 'https://seprab.com'
PATH = 'content'
TIMEZONE = 'America/Bogota'
DEFAULT_LANG = 'En'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DELETE_OUTPUT_DIRECTORY = False

# Blogroll
LINKS = (('Currently working on', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/PinguinoSepraB'),
          ('LinkedIn', 'https://www.linkedin.com/in/seprab/'),
          ('github', 'http://github.com/seprab'),)

# static paths will be copied without parsing their contents
STATIC_PATHS = ['static','assets']
EXTRA_PATH_METADATA = {
    'assets/images/favicon.ico': {'path': 'favicon.ico'},
    'assets/images/logo_only.png': {'path': 'logo_only.png'},
    'assets/images/banner.jpeg': {'path': 'banner.jpeg'},
    'assets/images/social_image.jpg': {'path': 'social_image.jpg'},
    }
RELATIVE_URLS = True
TEMPLATE_EXTENSIONS = ['.html']
PAGINATED_TEMPLATES = {
    'index': None,
    'tag': None,
    'category': None,
    'author': None,
}
DIRECT_TEMPLATES = ['index', 'archives', 'blog']

POST_LIMIT = 3

# Formatting for dates
DEFAULT_DATE_FORMAT = ('%d/%b/%Y %a')

# Formatting for urls

ARTICLE_URL = "{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{slug}/index.html"

# Plugins

PLUGIN_PATHS = ['D:\Personal\pelican-plugins']
PLUGINS = ['sitemap', 'neighbors', 'related_posts']


# Specify theme

THEME = "theme"
SWIFTYPE = ''
SITE_THUMBNAIL = 'logo_only.png'
SITE_THUMBNAIL_TEXT = 'SepraB'
SITESUBTITLE = 'Sergio Prada'

### Plugin-specific settings

RELATED_POSTS_MAX = 20

# TODO: align default SITEMAP config to http://wordpress.org/extend/plugins/google-sitemap-generator/stats/
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


#===theme settings===========================

FAVICON = 'assets/images/logo_background.png'
ICON = 'assets/images/logo_background.png'
SHORTCUT_ICON = 'assets/images/logo_background.png'

# About ME
PERSONAL_INFO = """My name is Sergio Prada, a Software Engineer at Unity Technologies. I'm working and living in Colombia. My experience has a variety of flavors because I started creating brand activation games, then I moved to the creation virtual simulators, later I worked on the creation of multi-platform applications for learning science, maths, etc, and now I'm providing professional support to the biggest customers of Unity in the Americas time zone.

I speak Spanish and English, I am an early parent, I love video games, movies, technology, challenges, outdoor activities and I plan to continue enjoying my life creating new things, enjoying my family, new technologies and nature."""

# work
WORK_DESCRIPTION = ""
# items to describe a work, "type", "cover-image link", "title", "descption", "link"
WORK_LIST = (
    ('link', 'assets/images/main_logo.png', 'BT3-Flat', 'Something else here', 'https://github.com/KenMercusLai/plumage'),
    ('link', 'assets/images/main_logo.png', 'BT3-Flat', 'Machine learning powered AI for simulating a tanks war', 'https://github.com/KenMercusLai/plumage'),
    ('link', 'assets/images/main_logo.png', 'BT3-Flat', 'COROVAMP', 'https://github.com/KenMercusLai/plumage'),
    )