from django import template
from django.urls import resolve
from main.models import MenuItem

register = template.Library()


def build_menu_tree(menu_items, current_url):
    tree = []
    image_tree = {}

    for item in menu_items:
        image_tree[item.id] = {'item': item, 'children': []}

    for item in menu_items:
        node = image_tree[item.id]
        if item.parent_id:
            image_tree[item.parent_id]['children'].append(node)
        else:
            tree.append(node)

    def set_active_nodes(node):
        node['is_active'] = (current_url == node['item'].get_url())

        for child in node['children']:
            if set_active_nodes(child):
                node['is_active'] = True

        return node['is_active']

    for node in tree:
        set_active_nodes(node)

    return tree


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_url = '/' + resolve(context['request'].path_info).url_name + '/'
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')
    menu_tree = build_menu_tree(menu_items, current_url)
    return {'menu_tree': menu_tree}
