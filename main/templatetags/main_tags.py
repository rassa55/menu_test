from django import template
from main.models import Menu

register = template.Library()

@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu = Menu.objects.filter(name=menu_name).prefetch_related('items__children').first()
    if menu:
        active_item = None
        for item in menu.items.all():
            if item.url == request.path:
                active_item = item
                break
        return {'menu': menu, 'active_item': active_item}
    return {'menu': None}