from django import template

register = template.Library()


@register.filter
def color(seed, month):
    return seed.coloring_cell(month)