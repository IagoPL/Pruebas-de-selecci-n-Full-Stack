from django.urls import path
from .views import post_user,get_users

urlpatterns = [
    path('post_user/', post_user, name='post_user'),
    path('get_users/', get_users, name='get_users'),
]
