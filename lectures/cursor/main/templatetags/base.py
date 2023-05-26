from datetime import datetime
from django import template

register = template.Library()


@register.simple_tag
def current_time(format_string):
    return datetime.now().strftime(format_string)