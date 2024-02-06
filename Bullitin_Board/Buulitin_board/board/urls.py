from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<int:cat_id>', PostCategory.as_view(), name='category'),
    path('post/<int:post_id>/', ShowPost.as_view(), name='post'),
    path('edit/<int:pk>/', EditPost.as_view(), name='edit'),
    path('add_post/', Add_Post.as_view(), name='add_post'),

]