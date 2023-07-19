from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.page, name="page"),
    path("error", views.error, name="error"),
    path("newPage", views.newPage, name="newPage"),
    path("randomPage", views.randomPage, name="randomPage"),
    path("searchPage", views.searchPage, name="searchPage"),
    path("editPage/<str:name>", views.editPage, name="editPage")
]
