from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.template.defaultfilters import stringfilter
from app import views

register = template.Library()
@register.filter(needs_autoescape=True)
@stringfilter
def highlight(value, search_query, autoescape=True):
    return mark_safe(value.replace(search_query, "<span class='highlight'>%s</span>" % search_query))
