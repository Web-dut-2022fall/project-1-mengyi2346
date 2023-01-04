from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:text_title>", views.text, name="text"),
    path("add/", views.add, name="add"),
    path("add/create", views.create, name="create"),
    path("search/", views.search, name="search"),
    path("rand/", views.rand, name="random"),
    path("edit/<str:text_title>", views.edit, name="editP")
]
