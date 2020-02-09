from django.urls import path
from Catalog.views import show_books, filter_book, book_details

urlpatterns = [
    path('', show_books, name='show_books'),
    path('ajax/filter_book/', filter_book, name='filter_book'),
    path('book_details/<book_id>', book_details, name='book_details'),
]