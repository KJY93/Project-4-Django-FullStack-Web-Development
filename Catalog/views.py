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
from el_pagination.decorators import page_template

@page_template('Catalog/entry_list_page.html') 
def show_books(request, template='Catalog/entry_list.html', extra_context=None):
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
    context = {
        'entry_list': books,
        'page_template': page_template,
        'genres': genres,
        'authors': author,
    }
    
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)



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
    
