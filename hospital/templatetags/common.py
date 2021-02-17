from django import template


register = template.Library()

@register.inclusion_tag("tags/bool_unknown.html")
def bool_unknown(label, val):
    return {"label": label, "val": val}

@register.simple_tag
def get_field_verbose_name(instance, field_name):
    return instance._meta.get_field(field_name).verbose_name
