from django import template


register = template.Library()


@register.filter(name='normalizeb64')
def normalize_base64(value, arg):
    return value.replace(arg, "")