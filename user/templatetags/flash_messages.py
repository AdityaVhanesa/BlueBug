from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter("filterTagError")
@stringfilter
def filterTag(value, arg):

    if arg in value.split():
        return True

    return False
