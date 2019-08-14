from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "store-home"),
    path('about/', views.about, name = "store-about"),
    path('login/', views.about, name = "store-login"),
]