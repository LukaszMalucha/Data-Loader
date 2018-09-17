from django.urls import path, include
from .views import mysql_loader, add_name, delete_names, add_document, manage_documents, database_upload


urlpatterns = [
    path('', mysql_loader, name="mysql_loader"),
    path('add_name', add_name, name="add_name"),
    path('delete_names', delete_names, name="delete_names"),
    path('add_document', add_document, name="add_document"),
    path('manage_documents', manage_documents, name="manage_documents"),
    path('database_upload/<file>', database_upload, name="database_upload")
    ]