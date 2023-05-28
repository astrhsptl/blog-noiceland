from django import template

register = template.Library()

@register.simple_tag
def lwq(link, query_param, pk):
    return f'{str(link)}?{str(query_param)}={str(pk)}'