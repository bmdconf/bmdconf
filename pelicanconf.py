#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'BMD Committee'
SITENAME = u'Bicycle and Motorcycle Dynamics Conference'
SITEURL = ''

PATH = 'content'
THEME = 'theme'
BOOTSTRAP_THEME = 'lumen'
CC_LICENSE = "CC-BY"
PAGE_ORDER_BY = 'sortorder'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

PASTCONFS = (
    ('BMD 2023 (Delft)', 'http://2023.bmdconf.org/'),
    ('BMD 2019 (Padua)',
     'https://web.archive.org/web/20240616130654/https://bmd2019.org/'),
    ('BMD 2016 (Milwaukee)',
     'https://web.archive.org/web/20190113222310/http://www.bmd2016mke.org/'),
    ('BMD 2013 (Narashino)',
     'https://web.archive.org/web/20141115093157/http://www.bmd2013.org/'),
    ('BMD 2010 (Delft)',
     'https://web.archive.org/web/20100529174822/http://bicycle.tudelft.nl/bmd2010'),
)

LINKS = (
    ('Polytechnic University<br>of Milan MOVE',
     'https://www.move.deib.polimi.it/'),
    ('TU Delft Bicycle Lab', 'http://bicycle.tudelft.nl'),
    ('Cornell Bicyce Mechanics',
     'http://ruina.tam.cornell.edu/research/topics/bicycle_mechanics/overview.php'),
    ('UW Milwaukee Bicycle and Motorcycle Engineering Research Laboratory',
     'http://people.uwm.edu/bike-motorcycle-lab/'),
    ('Rutgers Bicycle and Motorcycle Control Research',
     'http://coewww.rutgers.edu/~jgyi/'),
    ('Hochschule Karlsruhe Bike Lab',
     'https://www.h-ka.de/en/ieem/equipment/bike-lab'),
    ('Good Bicycle Science Blog', 'https://goodbicyclescience.com/'),
    ('Bad Bicycle Science Blog', 'https://badbicyclescience.com/'),
)

# Social widget
SOCIAL = (
    ('STVDY Listserv', 'https://groups.google.com/forum/#!forum/stvdy'),
)

SIDEBAR_IMAGES = ["/images/bmd-hor-logo-250x133.png"]

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
