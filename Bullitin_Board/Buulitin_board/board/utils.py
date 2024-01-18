from .models import *

menu = [
    {'title': 'Войти', 'url_name': 'home' },
    {'title': 'Выйти', 'url_name': 'search'},
    {'title': 'Регистрация', 'url_name': 'news'},
    {'title': 'Профиль', 'url_name': 'add_news'},

]


class DataMixin():

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        # if 'cat_selected' not in context:
        #     context['cat_selected'] = 0
        return context


