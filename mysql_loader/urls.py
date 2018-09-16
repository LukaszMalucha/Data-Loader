from django.urls import path, include
from .views import mysql_loader


urlpatterns = [
    path('', mysql_loader, name="mysql_loader"),
    ]