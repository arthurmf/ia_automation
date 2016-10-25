# -*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.filter(name='filtro_teste')
def filtro_teste(d, args):
    return "%s" %(d[args])