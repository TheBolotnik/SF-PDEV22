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

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('news/', newslist, name='news'),
    path('add_news/', add_news, name='add_news'),
    path('login', login, name='login'),
    path('post/<int:post_id>/', post, name='post'),
    path('category/<int:cats_id>', category, name='category'),


    #path('/newslist', NewsList, name=NewsList),
    #path('news/', views.NewsList.as_view()),
    #path('pages/', include('django.contrib.flatpages.urls')),


]