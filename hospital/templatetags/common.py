from django import template

from users.models import User


register = template.Library()

@register.inclusion_tag("tags/bool_unknown.html")
def bool_unknown(label, val):
    return {"label": label, "val": val}

@register.inclusion_tag("tags/select2ify.html")
def select2ify(id):
    return {"id": id}

@register.inclusion_tag("tags/orderable_header.html")
def orderable_header(name, label, width=None):
    return {"name": name, "label": label, "width": width}

@register.simple_tag
def get_field_verbose_name(instance, field_name):
    return instance._meta.get_field(field_name).verbose_name

@register.simple_tag
def is_admin(user):
    if isinstance(user, User) and user.role == User.ROLE_ADMIN:
        return True
    return False
