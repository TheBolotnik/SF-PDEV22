from django.urls import path, include

import allauth

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    ]

