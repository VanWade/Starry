from django import template
from django.utils.safestring import mark_safe
import markdown


register = template.Library()

from twinkle.models import Twinkle

@register.simple_tag
def total_twinkles():
    return Twinkle.published.count()

@register.inclusion_tag('twinkle/Twinkle/latest_twinkles.html')
def show_latest_twinkles(count=5):
    latest_twinkles = Twinkle.published.order_by('-publish')[:count]
    return {'latest_twinkles': latest_twinkles}

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


