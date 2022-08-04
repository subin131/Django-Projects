from django.urls import path
from login import views

urlpatterns = [
     path("add/",views.add,name="add"),
     path("display/",views.display,name="display"),
     path("delete/<int:id>/",views.delete,name="delete"),
     # path("edit/<int:id>/",views.edit,name="edit"),
     
]
