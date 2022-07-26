from django.urls import path
from hot_app import views

urlpatterns = [
   path("home/",views.home,name="home"),
   path("display/",views.display,name="display"),
]
