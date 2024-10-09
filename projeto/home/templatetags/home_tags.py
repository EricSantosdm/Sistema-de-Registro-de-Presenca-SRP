from django import template
from django.conf import settings
from srp_app.models import Evento

register = template.Library()


@register.simple_tag()
def eventos():
    """Retorna os eventos."""
    return Evento.objects.all()


@register.simple_tag()
def is_dev():
    """Retorna True se o ambiente for de desenvolvimento."""
    return settings.DEV


@register.filter()
def get_dict_item(dictionary, key):
    """Retorna o valor de um item de um dicionário."""
    value = dictionary.get(key, None)
    if value is None or value == "":
        return "-"

    return dictionary.get(key)


@register.simple_tag()
def get_dict_item_tag(dictionary, key):
    """Retorna o valor de um item de um dicionário."""
    value = dictionary.get(key, None)
    if value is None or value == "":
        return "-"

    return dictionary.get(key)
