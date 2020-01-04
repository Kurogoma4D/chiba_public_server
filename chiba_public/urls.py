from django.urls import path
from chiba_public import views

urlpatterns = [
    path("", views.home, name="home"),
]
