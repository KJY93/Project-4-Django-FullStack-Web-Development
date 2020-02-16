from django.urls import path
# 160220 add in book filter
from Catalog.views import show_books, book_details, book_filter

urlpatterns = [
    # change from '' to <category> to cater for different category based on user selection
    path('<category>', show_books, name='show_books'),
    path('book_details/<book_id>', book_details, name='book_details'),
    # add in book filter route
    path('filter/', book_filter, name='filter'),
]