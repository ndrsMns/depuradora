from django import template

register = template.Library()

@register.filter
def label_vb(instance, arg):
    return instance._meta.get_field(arg).verbose_name