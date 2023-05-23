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
# LINKS = (('Currently working on', '#'),)

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
#     'author': None,
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
WORK_DESCRIPTION = "This is a quick mention to projects where I participated or I am participating. Showing projects where I worked is not an easy task due to non-disclosure agreements or simply no public web reference to it. In case you'd like to better understand my experience visit my LinkedIn profile or visit the last item in this section."
# items to describe a work, "type", "cover-image link", "title", "descption", "link"
WORK_LIST = (
    ('link', 'https://scontent.fbog7-1.fna.fbcdn.net/v/t39.30808-6/299874384_381916974098494_1045593393974149491_n.png?_nc_cat=104&ccb=1-7&_nc_sid=e3f864&_nc_eui2=AeEw_Sw71YdRqn1VVQdQckf3E5t6By6Y-pATm3oHLpj6kP-RTiDVsijn5t3XPp-Un0E&_nc_ohc=TOGRv97E0QsAX_S-NuK&_nc_ht=scontent.fbog7-1.fna&oh=00_AfBGa9VpH_1zZNf2j11y5MOsJKHcgJwzxqhwL4cKLc85CA&oe=6470BA68', 'Tamaguino', "I'm working on a customized version of Tamaguino for my son based on Alojz Jakob development. Also, this is a oportunity to get to know arduino with C++", "https://github.com/seprab/Tamaguino"),
    ('link', 'https://i9.ytimg.com/vi_webp/fmvXJ-wFV9s/mq1.webp?sqp=CLDYsKMG&rs=AOn4CLCUPbZLfY40La13bmMmSinceT4gGA', 'ML-trained Tanks', 'Machine learning powered AI for simulating a tanks war. This was my final project after participating in a data analytics course with IronHack', 'https://www.youtube.com/watch?v=fmvXJ-wFV9s'),
    ('link', 'https://www.msholdinggroup.com/wp-content/uploads/2018/06/CAS2.jpg', 'CAS', "I participated in the development of an artillery simulator", 'https://www.msholdinggroup.com/solutions/simulation/cas/'),
    ('link', 'https://img.itch.zone/aW1hZ2UvNTk4MTgwLzMxNjc2MDYucG5n/347x500/%2BfUSmN.png', 'COROVAMP', "This is quick participation with two friends in a Colombian game jam. Worth mentioning that I enjoyed participating in it with them and they did not know how to use Unity", 'https://chechogordillo.itch.io/corovamp'),
    ('link', 'https://cloudlabs.us/wp-content/uploads/2022/04/Control-de-Procesos-EN.jpg', 'Virtual Laboratories', "I worked with ToroLabs for migrating some virtual laboratories to Unity, and in some other cases develop a new course", 'https://cloudlabs.us/'),
    ('link', 'https://www.msholdinggroup.com/wp-content/uploads/2018/05/screen6.jpg', 'TRACTORSIM®', "I participated in the development of a tractor simulator", 'https://youtu.be/mI9MLGqo7BE'),
    ('link', 'https://yt3.googleusercontent.com/BAwufudedvzhF9w3vl_RxSUAghXpXIU-OwmZzM67jjgdUNSVdpRopdic4Q85uE26WQpUuZSHzQ=w2120-fcrop64=1,00005a57ffffa5a8-k-c0xffffffff-no-nd-rj', 'ROOM SCALE', "This is one of multiple minor projects where I participated. We were exploring the possibility to pre-visualize, navigate and interact with a virtual location.", 'https://youtu.be/mI9MLGqo7BE'),
    ('link', 'https://seprab.com/social_image.jpg', 'My timeline', "Give it a look. I tried to keep it as simple as possible and easy to understand.", 'https://seprab.com/2023/03/seprabs-timeline/'),
    )