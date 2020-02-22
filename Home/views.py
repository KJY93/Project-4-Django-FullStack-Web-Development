from django.shortcuts import render
from Catalog.models import Book
from Order.models import OrderItem
import datetime

import dateutil.relativedelta

def get_index(request):
    # get the previously ordered items
    ordered_items_list = []
    for product in Book.objects.all():
        if len(product.order_items.all()) > 0:
            ordered_items_list.append(sorted([dict(quantity=sum([item.quantity for item in product.order_items.all()]), book_id=product.id)],
            key=lambda k: k['quantity'], reverse=True))
            
    # filter out top 10 bestselling books
    ordered_items_list = ordered_items_list[0:10]
    
    # get associated book id
    book_id_list = []
    
    # loop through the above dictionary and get only the book id
    for bk_id in ordered_items_list:
        book_id_list.append(bk_id[0]['book_id'])
    
    # loop through the Book object and filter out the top 10 best sellers by book id from above
    bestsellers = Book.objects.filter(pk__in=book_id_list)
    
    # new and trending books (last 6 months up to current)
    current_year_month_date = datetime.datetime.now()
    last_6_month = current_year_month_date + dateutil.relativedelta.relativedelta(months=-6)

    current_year = current_year_month_date.year
    current_month = current_year_month_date.month
    current_day = current_year_month_date.day
    
    last_6_month_year = last_6_month.year
    last_6_month_month = last_6_month.month
    last_6_month_day = last_6_month.day   

    new_and_trending = Book.objects.filter(publishing_year__gte=datetime.date(last_6_month_year, last_6_month_month, last_6_month_day),
                                publishing_year__lte=datetime.date(current_year, current_month, current_day))
    
    # best deals book
    best_deal_book = Book.objects.filter(price__lte=5.00)

    return render(request, 'Home/index.template.html', {
        'bestsellers':bestsellers,
        'new_and_trending':new_and_trending,
        'best_deal_book':best_deal_book
    })
    
    
def our_service(request):
    return render(request, 'Home/our-services.html')
    
def about_us(request):
    return render(request, 'Home/about-us.html')
    
def contact_us(request):
    return render(request, 'Home/contact-us.html')