from django.urls import path
from Catalog.views import show_books, filter_book

urlpatterns = [
    path('', show_books, name='show_books'),
    path('ajax/filter_book/', filter_book, name='filter_book'),
]