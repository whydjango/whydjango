# -*- coding: utf-8 -*-
# language codes according to ISO 639
# see http://www.loc.gov/standards/iso639-2/php/English_list.php for reference
_ = lambda s: s
ALL_LANGUAGES = dict((
    # DJANGO DEFAULTS (django.conf.global_settings.LANGUAGES)
    ('ar',    _('Arabic')),
    ('bg',    _('Bulgarian')),
    ('bn',    _('Bengali')),
    ('bn',    _('Bosnian')),
    ('ca',    _('Catalan')),
    ('cs',    _('Czech')),
    ('cy',    _('Welsh')),
    ('da',    _('Danish')),
    ('de',    _('German')),
    ('el',    _('Greek')),
    ('en',    _('English')),
    ('es',    _('Spanish')),
    ('es-ar', _('Argentinean Spanish')),
    ('et',    _('Estonian')),
    ('eu',    _('Basque')),
    ('fa',    _('Persian')),
    ('fi',    _('Finnish')),
    ('fr',    _('French')),
    ('fy-nl', _('Frisian')),
    ('ga',    _('Irish')),
    ('gl',    _('Galician')),
    ('he',    _('Hebrew')),
    ('hi',    _('Hindi')),
    ('hr',    _('Croatian')),
    ('hu',    _('Hungarian')),
    ('is',    _('Icelandic')),
    ('it',    _('Italian')),
    ('ja',    _('Japanese')),
    ('ka',    _('Georgian')),
    ('km',    _('Khmer')),
    ('kn',    _('Kannada')),
    ('ko',    _('Korean')),
    ('lt',    _('Lithuanian')),
    ('lv',    _('Latvian')),
    ('mk',    _('Macedonian')),
    ('nl',    _('Dutch')),
    ('no',    _('Norwegian')),
    ('pl',    _('Polish')),
    ('pt',    _('Portuguese')),
    ('pt-br', _('Brazilian Portuguese')),
    ('ro',    _('Romanian')),
    ('ru',    _('Russian')),
    ('sk',    _('Slovak')),
    ('sl',    _('Slovenian')),
    ('sq',    _('Albanian')),
    ('sr',    _('Serbian')),
    ('sr-latn', _('Serbian Latin')),
    ('sv',    _('Swedish')),
    ('ta',    _('Tamil')),
    ('te',    _('Telugu')),
    ('th',    _('Thai')),
    ('tr',    _('Turkish')),
    ('uk',    _('Ukrainian')),
    ('zh-cn', _('Simplified Chinese')),
    ('zh-tw', _('Traditional Chinese')),
    # EXTRA LANGUAGES
    ('bs',    _('Bosnian')),
    ('de-ch', _('Swiss German')),
    ('fr-ch', _('Swiss French')),
))

MULTILINGUAL_FALLBACK_LANGUAGES = {
    'en': ['en',],
}
CMS_LANGUAGE_CONF = MULTILINGUAL_FALLBACK_LANGUAGES
CMS_SITE_LANGUAGES = { # SITE_ID: [LANGUAGE_CODE_LIST]
    1: ['en',], # main
}

DEFAULT_LANGUAGE = 0
LANGUAGE_CODE = 'en'

# auto build LANGUAGES based on ALL_LANGUAGES and all languages used in 
# CMS_SITE_LANGUAGES
LANGUAGES = []
ALL_USED_LANGUAGE_CODES = []
for site_id, langs in CMS_SITE_LANGUAGES.items():
    for lang in langs:
        if not lang in ALL_USED_LANGUAGE_CODES:
            ALL_USED_LANGUAGE_CODES.append(lang)
ALL_USED_LANGUAGE_CODES.sort()
for lang in ALL_USED_LANGUAGE_CODES:
    LANGUAGES.append( ( lang, ALL_LANGUAGES[lang] ) )