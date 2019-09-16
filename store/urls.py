from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name = "store-home"),
    path('about/', views.about, name = "store-about"),
    path('book/', views.book, name = "store-book"),
    path('register/', views.user_register, name='user_register'), # maybe change
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('rentals/', views.user_rentals, name='user_rentals'),
    path('returns/', views.user_returns, name='user_returns'),



]
