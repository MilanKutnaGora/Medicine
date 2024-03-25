import os

from django import template
from django.conf import settings

register = template.Library()


@register.filter(name='path_to_media')
def path_to_media(val):
    if val:
        return f'/media/{val}'
    return '/media/no_image.png'


@register.simple_tag()
def mymedia(val):
    if val:
        return f'/media/{val}'
    return '/media/no_image.png'