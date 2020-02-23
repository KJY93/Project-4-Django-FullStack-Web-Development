from django.urls import path, include
from .views import checkout, confirm_checkout

urlpatterns = [
    path('', checkout, name='checkout'),
    path('confirm_checkout/', confirm_checkout, name='confirm_checkout'),    
]