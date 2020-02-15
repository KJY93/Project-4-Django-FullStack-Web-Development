from django.urls import path
from Carts.views import add_to_cart, view_cart, remove_from_cart, update_cart

urlpatterns = [
     path('add/<book_id>', add_to_cart, name='add_to_cart'),
     path('remove/<book_id>', remove_from_cart, name='remove_from_cart'),
     path('', view_cart, name='view_cart'),
     path('update/<book_id>', update_cart, name='update_cart')
]