from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),  # Connects the root URL to your view
]
