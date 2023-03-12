AUTHOR = 'SepraB'
SITENAME = "SepraB's"
SITEURL = 'https://seprab.github.io/seprab/'

PATH = 'content'

TIMEZONE = 'America/Bogota'

DEFAULT_LANG = 'En'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('CV', '#'),
         ('Currently working on', '#'),)

# Social widget
SOCIAL = (('Twiter', 'https://twitter.com/PinguinoSepraB'),
          ('LinkedIn', 'https://www.linkedin.com/in/seprab/'),
          ('Mail', 'sergioeprada@hotmail.com'))

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'static',
    ]


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True