from .models import Category

menu = [
    {'title': 'Главная страница', 'url_name': 'home' },
    {'title': 'Новости', 'url_name': 'news'},
    {'title': 'Добавить новость', 'url_name': 'add_news'},
    {'title': 'Войти', 'url_name': 'login'},
    {'title': 'Поиск', 'url_name': 'search'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context