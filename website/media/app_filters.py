# -*- coding: utf-8 -*-

from django import template

register = template.Library()

@register.filter(name='filtro_teste')
def filtro_teste(d, args):
    return "%s" %(d[args])
    
@register.filter(name='get_dict_value')
def get_dict_value(dict, args):
    return dict[args]