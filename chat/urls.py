from django.urls import path
from . import views

urlpatterns = [
    path('', views.set_nickname, name='set_nickname'),
    path('chat/', views.chatroom, name='chatroom'),
]
