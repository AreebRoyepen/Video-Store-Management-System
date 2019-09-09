from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name = "store-home"),
    path('about/', views.about, name = "store-about"),
    path('book/', views.book, name = "store-book"),
    path('register/', views.user_register, name='user_register'), # maybe change
    path('login/', views.user_login, name='user_login')

]
