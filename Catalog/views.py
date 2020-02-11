from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from .models import Book, Genre, Author
from django.contrib.auth.decorators import login_required
import absoluteuri
from django.http import JsonResponse
from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
from django.conf import settings
from django.template.loader import render_to_string


def show_books(request):
    
    books = Book.objects.all().order_by('-publishing_year')
    genres = Genre.objects.all()
    author = Author.objects.all()

    # filter option on
    if ('genre_selected[]' in request.GET):
        books = Book.objects.filter(genre__category_description__in=request.GET.getlist('genre_selected[]'))

    if ('author_selected[]' in request.GET):
        books = Book.objects.filter(author__name__in=request.GET.getlist('author_selected[]'))

    if ('from_price' in request.GET) or ('to_price' in request.GET):
        if int(request.GET.get('to_price')) > 0:
            books = Book.objects.filter(price__range=(int(request.GET.get('from_price')), int(request.GET.get('to_price'))))
    
    # if option is reset (i.e. no option is selected)
    if ('genre_selected[]' not in request.GET) and ('author_selected[]' not in request.GET):
        if ('to_price' in request.GET):
            if int(request.GET.get('to_price')) == 0:
                books = Book.objects.all().order_by('-publishing_year')
                
    book_list = books

    # Show 8 books per page 
    paginator = Paginator(book_list, 8)  

    page = request.GET.get('page', 1)

    try:
        book_qs = paginator.page(page)
    except PageNotAnInteger:
        book_qs = paginator.page(1)
    except EmptyPage:
        book_qs = paginator.page(paginator.num_pages)

    # in case of ajax call update show_books.template.html page
    if request.is_ajax():
        html = render_to_string('Catalog/filtered_books.template.html', {'book_qs': book_qs})
        return HttpResponse(html)

    return render(request, 'Catalog/show_books.template.html', {
        'all_books':books,
        'genres':genres,
        'authors':author,
        'book_qs': book_qs,
    })

def book_details(request, book_id):
    book_detail = Book.objects.filter(id=int(book_id))

    book_genre = list(book_detail.values('genre__category_description'))[0]['genre__category_description']

    book_ISBN = list(book_detail.values('ISBN'))[0]['ISBN']

    # get book ratings from GoodReads using GoodReads API
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key":settings.GOODREADS_API_KEY, "isbns": book_ISBN})
    average_ratings = res.json()["books"][0]["average_rating"]

    return render(request, 'Catalog/show_book_details.template.html', {
        'book_detail':book_detail,
        'average_ratings':average_ratings,
        'book_genre': book_genre
    })