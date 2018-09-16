from django.urls import path, include
from .views import mysql_loader, add_name


urlpatterns = [
    path('', mysql_loader, name="mysql_loader"),
    path('add_name', add_name, name="add_name"),
    ]