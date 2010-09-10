from django.utils.encoding import force_unicode
from django import template
import re

register = template.Library()

def intsep(value, sep="'"):
    orig = force_unicode(value)
    new = re.sub("^(-?\d+)(\d{3})", '\g<1>%s\g<2>' % sep, orig)
    if orig == new:
        return new
    else:
        return intsep(new)
intsep.is_safe = True
register.filter(intsep)

def crop_empty_comma(value, fill=""):
    orig = force_unicode(value)
    if not '.' in orig:
        return orig
    before, after = orig.rsplit('.', 1)
    if after.strip('0'):
        return orig
    return u'%s%s' % (before, fill)
crop_empty_comma.is_safe = True
register.filter(crop_empty_comma)