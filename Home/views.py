from django.shortcuts import render
# from Catalog.models import Book, BookCover
from Catalog.models import Book
import datetime
# from datetime import date, timedelta

import dateutil.relativedelta

def get_index(request):
    # bestsellers = Book.objects.all().order_by('book_ratings')
    # need to edit this later to follow the the orderItem
    bestsellers = Book.objects.all()
    
    # new and trending books (last 3 months up to current)
    current_year_month_date = datetime.datetime.now()
    last_3_month = current_year_month_date + dateutil.relativedelta.relativedelta(months=-3)

    current_year = current_year_month_date.year
    current_month = current_year_month_date.month
    current_day = current_year_month_date.day
    
    last_3_month_year = last_3_month.year
    last_3_month_month = last_3_month.month
    last_3_month_day = last_3_month.day   

    new_and_trending = Book.objects.filter(publishing_year__gte=datetime.date(last_3_month_year, last_3_month_month, last_3_month_day),
                                publishing_year__lte=datetime.date(current_year, current_month, current_day))
    
    # best deals book
    best_deal_book = Book.objects.filter(price__lte=5.00)

    return render(request, 'Home/index.template.html', {
        'bestsellers':bestsellers,
        'new_and_trending':new_and_trending,
        'best_deal_book':best_deal_book
    })
    