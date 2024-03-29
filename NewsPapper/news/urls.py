"""NewsPapper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', NewsHome.as_view(), name='home'),
    path('news/', NewsList.as_view(), name='news'),
    path('news/create/', AddNews.as_view(), name='add_news'),
    path('news/<int:pk>/edit/', NewsEdit.as_view(), name='edit_news'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='delete_news'),
    path('news/search', Search.as_view(), name='search'),
    path('post/<int:post_id>/', ShowPost.as_view(), name='post'),
    path('category/<int:cat_id>', NewsCategory.as_view(), name='category'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('signin/', SignIn.as_view(), name='signin'),
    path('news/create/upgrade/', upgrade_authors, name='upgrade'),
    path('category/<int:cat_id>/subscribe', subscribe, name='subscribe'),
    path('category/<int:cat_id>/unsubscribe', unsubscribe, name='unsubscribe'),

    #path('profile/', UserProfile.as_view(), name='profile')


]