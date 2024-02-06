from .models import *

menu = [
    {'title': 'Войти', 'url_name': 'home' },
    {'title': 'Выйти', 'url_name': 'search'},
    {'title': 'Регистрация', 'url_name': 'news'},
    {'title': 'Профиль', 'url_name': 'add_news'},

]

profile_menu = [
    {'title': "Добавить объявление", 'url_name': 'add_post'},
    {'title': "Войти", 'url_name': 'login'},
    {'title': "Регистрация", 'url_name': 'signin'},
    {'title': "Профиль", 'url_name': 'profile'},

]


class DataMixin():

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        context['profile_menu'] = profile_menu
        # if 'cat_selected' not in context:
        #     context['cat_selected'] = 0
        return context


def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}
