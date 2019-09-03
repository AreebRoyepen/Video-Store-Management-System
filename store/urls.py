from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "store-home"),
    path('about/', views.about, name = "store-about"),
    path('login/', views.login, name = "store-login"),
    path('register/', views.register, name = "store-register"),
    path('book/', views.book, name = "store-book")
]