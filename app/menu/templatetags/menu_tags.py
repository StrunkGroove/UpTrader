from django import template

from ..services import MenuBuilder


register = template.Library()


@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu(context, menu_name: str):
    requested_url = context['request'].path
    builder = MenuBuilder()
    return builder.build_menu(requested_url, menu_name)