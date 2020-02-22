from django.urls import path
from .views import show_books, book_details

urlpatterns = [
    path('', show_books, name='show_books'),
    path('book_details/<book_id>', book_details, name='book_details'),
]