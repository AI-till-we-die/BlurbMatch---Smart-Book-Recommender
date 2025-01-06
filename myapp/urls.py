from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("recommend-books/", views.recommend_books, name="recommend_books"),
]
