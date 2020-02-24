from django.urls import path, include
from .views import checkout, confirm_checkout, view_purchase_list, view_purchase_details, update_order

urlpatterns = [
    path('', checkout, name='checkout'),
    path('confirm_checkout/', confirm_checkout, name='confirm_checkout'),   
    path('view_purchase_list/', view_purchase_list, name='view_purchase_list'),
    path('view_purchase_details/<order_purchase_id>', view_purchase_details, name='view_purchase_details'),    
    path('update_order/<order_id>', update_order, name='update_order'),   
]