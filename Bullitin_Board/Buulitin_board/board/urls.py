from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    #path('category/<int:cat_id>/', show_category, name='category'),
    path('category/<int:cat_id>', PostCategory.as_view(), name='category'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('add_post/', add_post, name='add_post'),
    path('login/', login, name='login'),
    path('signin/', signin, name='signin'),
    path('profile/', profile, name='profile'),
]