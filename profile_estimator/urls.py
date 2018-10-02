from django.urls import path, include
from .views import profile, estimate


urlpatterns = [
    path('', profile, name="profile"),
    path('estimate', estimate, name="estimate")
    ]