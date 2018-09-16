from django.urls import path, include
from .views import mongo_loader

urlpatterns = [
    path('', mongo_loader, name="mongo_loader"),
    ]