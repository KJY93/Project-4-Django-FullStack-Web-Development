from django.urls import path, include
from .views import checkout

urlpatterns = [
    path('', checkout, name='checkout')
]