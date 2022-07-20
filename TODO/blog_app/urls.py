from blog_app import views
from django.urls import path

urlpatterns = [
    path("home/",views.home,name="home"),
    path("add/",views.add,name="add")
]