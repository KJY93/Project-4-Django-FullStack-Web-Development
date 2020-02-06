from django.shortcuts import render
# from Catalog.models import Book, BookCover
from Catalog.models import Book
import datetime

def get_index(request):
    # bestsellers = Book.objects.all().order_by('book_ratings')
    # need to edit this later to follow the the orderItem
    bestsellers = Book.objects.all()
    
    # new and trending books
    current_year = datetime.datetime.now().year
    previous_year = current_year - 1
    
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day    

    new_and_trending = Book.objects.filter(publishing_year__gte=datetime.date(previous_year, month, day),
                                publishing_year__lte=datetime.date(current_year, month, day))
                                
    # best deals book
    best_deal_book = Book.objects.filter(price__lte=5.00)

    return render(request, 'Home/index.template.html', {
        'bestsellers':bestsellers,
        'new_and_trending':new_and_trending,
        'best_deal_book':best_deal_book
    })
    