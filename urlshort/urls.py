from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<str:url>', views.my_redirect),
    path('geturl/', views.createShortURL),
]