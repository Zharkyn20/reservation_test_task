from django.template import Library

register = Library()


@register.filter
def get_value(dict, key):
    return dict.get(key)
