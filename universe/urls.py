
from django.urls import path
from .views import board, comment_page, main

urlpatterns = [
    path('', main, name='main'),
    path('board/', board, name='board'),
    path('comment_page/',comment_page,name='comment_page'),
]