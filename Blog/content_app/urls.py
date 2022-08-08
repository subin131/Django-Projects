from django.urls import path
from content_app import views
urlpatterns = [
    path("home/",views.home,name="home"),
    path("add/",views.add,name="add"),
    path("edit/<int:id>/",views.edit,name="edit"),
  
]
