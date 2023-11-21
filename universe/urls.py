
from django.urls import path
from .views import board, comment_page, main, post

urlpatterns = [
    path('', main, name='main'),
    path('board/', board, name='board'),
    path('comment_page/',comment_page,name='comment_page'),
    path('post/',post, name='post')
]