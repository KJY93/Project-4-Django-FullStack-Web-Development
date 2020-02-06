from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from .models import Book, Genre, Author

from django.contrib.auth.decorators import login_required

def show_books(request):
    
    all_books = Book.objects.all().order_by('publishing_year')
    
    return render(request, 'Catalog/show_books.template.html', {
        'all_books':all_books,
    })