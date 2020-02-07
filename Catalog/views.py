from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from .models import Book, Genre, Author

from django.contrib.auth.decorators import login_required

def show_books(request):
    
    all_books = Book.objects.all()
    genres = Genre.objects.all()
    author = Author.objects.all()
    
    return render(request, 'Catalog/show_books.template.html', {
        'all_books':all_books,
        'genres':genres,
        'authors':author
    })