from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from .models import Book, Genre, Author
from django.contrib.auth.decorators import login_required
import absoluteuri
from django.http import JsonResponse

# 0802
from django.db import models

def show_books(request):

    all_books = Book.objects.all()
    genres = Genre.objects.all()
    author = Author.objects.all()

    return render(request, 'Catalog/show_books.template.html', {
        'all_books':all_books,
        'genres':genres,
        'authors':author,
        'path_uri': absoluteuri.build_absolute_uri(reverse('filter_book'))
    })

def filter_book(request):
    
    if len(request.GET) == 0:
        filtered_book = Book.objects.all()
        
    if ('genre_selected[]' in request.GET) and ('author_selected[]' in request.GET):
        filtered_book = Book.objects.filter(genre__category_description__in=request.GET.getlist('genre_selected[]')) | Book.objects.filter(author__name__in=request.GET.getlist('author_selected[]'))

    if ('genre_selected[]' in request.GET) and ('author_selected[]' not in request.GET):
        filtered_book = Book.objects.filter(genre__category_description__in=request.GET.getlist('genre_selected[]'))
        
    if ('author_selected[]' in request.GET) and ('genre_selected[]' not in request.GET):
        filtered_book = Book.objects.filter(author__name__in=request.GET.getlist('author_selected[]'))

    # https://stackoverflow.com/questions/42980477/django-select-related-query-does-not-return-all-values-to-the-template
    # need to specifically list out all the values you want, it does not implicitly include foreign key by default
    serialized = list(filtered_book.values('id', 'author__name', 'title', 'publisher', 'quantity', 'pages', 'ISBN', 
    'genre__category_description', 'description', 'publishing_year', 'price', 'image'))
    return JsonResponse(serialized, safe=False)
    