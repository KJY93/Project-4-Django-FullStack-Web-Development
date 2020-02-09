from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from .models import Book, Genre, Author
from django.contrib.auth.decorators import login_required
import absoluteuri
from django.http import JsonResponse

from django.db import models

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# 0902
import requests
from django.conf import settings


def show_books(request):
    all_books = Book.objects.all().order_by('-publishing_year')
    
    # pagination setup show 9 books per page
    paginator = Paginator(all_books, 8)
    page = request.GET.get('page')
    
    try:
        book_qs = paginator.page(page)
    except PageNotAnInteger:
        book_qs = paginator.page(1)
    except EmptyPage:
        book_qs = paginator.page(paginator.num_pages)
    # end of pagination setup

    page = request.GET.get('page', 1)
    genres = Genre.objects.all()
    author = Author.objects.all()
    
    return render(request, 'Catalog/show_books.template.html', {
        'all_books':all_books,
        'genres':genres,
        'authors':author,
        'book_qs':book_qs,
        'path_uri': absoluteuri.build_absolute_uri(reverse('filter_book'))
    })

def filter_book(request):
    
    if len(request.GET) == 0:
        filtered_book = Book.objects.all()
        
    if ('genre_selected[]' in request.GET):
        filtered_book = Book.objects.filter(genre__category_description__in=request.GET.getlist('genre_selected[]'))
        
        if ('author_selected[]' in request.GET):
            filtered_book = Book.objects.filter(author__name__in=request.GET.getlist('author_selected[]'))
        
        if ('from_price' in request.GET) or ('to_price' in request.GET):
            if int(request.GET.get('to_price')) > 0:
                filtered_book = Book.objects.filter(price__range=(int(request.GET.get('from_price')), int(request.GET.get('to_price')))) 
      
    if ('author_selected[]' in request.GET):          
        filtered_book = Book.objects.filter(author__name__in=request.GET.getlist('author_selected[]'))

        if ('genre_selected[]' in request.GET):
            filtered_book = Book.objects.filter(genre__category_description__in=request.GET.getlist('genre_selected[]'))
            
        if ('from_price' in request.GET) or ('to_price' in request.GET):
            if int(request.GET.get('to_price')) > 0:
                filtered_book = Book.objects.filter(price__range=(int(request.GET.get('from_price')), int(request.GET.get('to_price')))) 
                
    if ('from_price' in request.GET) or ('to_price' in request.GET):
        if int(request.GET.get('to_price')) > 0:
            filtered_book = Book.objects.filter(price__range=(int(request.GET.get('from_price')), int(request.GET.get('to_price')))) 
            
        if ('author_selected[]' in request.GET):
            filtered_book = Book.objects.filter(author__name__in=request.GET.getlist('author_selected[]'))
            
        if ('genre_selected[]' in request.GET):
            filtered_book = Book.objects.filter(genre__category_description__in=request.GET.getlist('genre_selected[]'))
                
    # https://stackoverflow.com/questions/42980477/django-select-related-query-does-not-return-all-values-to-the-template
    # need to specifically list out all the values you want, it does not implicitly include foreign key by default
    serialized = list(filtered_book.values('id', 'author__name', 'title', 'publisher', 'quantity', 'pages', 'ISBN', 
    'genre__category_description', 'description', 'publishing_year', 'price', 'image'))
    return JsonResponse(serialized, safe=False)
    
# 0902
def book_details(request, book_id):
    book_detail = Book.objects.filter(id=int(book_id))
    
    book_ISBN = list(book_detail.values('ISBN'))[0]['ISBN']
    
    # get book ratings from GoodReads using GoodReads API
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key":settings.GOODREADS_API_KEY, "isbns": book_ISBN})
    average_ratings = res.json()["books"][0]["average_rating"]
    
    return render(request, 'Catalog/show_book_details.template.html', {
        'book_detail':book_detail,
        'average_ratings':average_ratings
    })