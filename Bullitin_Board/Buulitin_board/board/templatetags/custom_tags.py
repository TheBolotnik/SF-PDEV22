from django import template

from board.models import Category

register = template.Library()


@register.inclusion_tag('board/category.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}

