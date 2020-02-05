from django.urls import path
from Catalog.views import show_books

urlpatterns = [
    path('', show_books, name='show_books')
]