from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name = "store-home"),
    path('about/', views.about, name = "store-about"),
    path('login/', views.login, name = "store-login"),
    path('register/', views.register, name = "store-register"),
    path('book/', views.book, name = "store-book")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
