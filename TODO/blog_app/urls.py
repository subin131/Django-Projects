from blog_app import views
from django.urls import path

urlpatterns = [
    path("home/",views.home,name="home"),
    path("add/",views.add,name="add"),
    path("delete/<int:id>/",views.delete,name="delete"),
    path("edit/<int:id>/",views.edit,name="edit"),
    path("delete-all/",views.delete_all,name="delete-all"),
]