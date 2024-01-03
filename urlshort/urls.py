from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<str:url>', views.redirect),
    path('geturl/', views.createShortURL),
]