from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.page, name="page"),
    path("newPage", views.newPage, name="newPage"),
    path("randomPage", views.randomPage, name="randomPage"),
    #path("editPage/<str:name>", views.editPage, name="editPage")
]
