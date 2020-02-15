import json
import absoluteuri
from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from django.contrib import messages
from Catalog.models import Book
from django.core import serializers
from django.http import JsonResponse
from django.template.loader import render_to_string

# 120220
def view_cart(request):
    
    # retrieve shopping cart info
    cart = request.session.get('shopping_cart', {})
    
    return render(request, 'Carts/view_cart.template.html', {
        'shopping_cart':cart
    })
    
def add_to_cart(request, book_id):

    cart = request.session.get('shopping_cart', {})
    
    if book_id not in cart:
        book = get_object_or_404(Book, pk=book_id)
        
        # get the book author
        authors = book.author.all()
        serialized_authors = (serializers.serialize('json', authors))
        authors = json.loads(serialized_authors)
        
        if len(authors) > 1:
            authors_list = []
            
            for i in range(len(authors)):
                authors_list.append(authors[i]['fields']['name'])
            authors_list = " & ".join(authors_list)
        else:
            authors_list = authors[0]['fields']['name']
    
        # if book exist, then add it to the shopping cart
        cart[book_id] = {
            
            'id': book_id,
            'title': book.title,
            # need to convert decimal field to float field due to Decimal field is not serializable in JSON
            'price': float("{0:.2f}".format(book.price)),
            
            # original quantity
            # 140220
            'original_quantity':book.quantity,
            
            # available quantity
            # 140220 update quantity based on user purchase
            'available_quantity':book.quantity - int(request.POST.get("quantity")),
            
            # get the quantity ordered ordered through form submission 1202
            'quantity_ordered': int(request.POST.get("quantity")), 
            
            # get total price
            'total_price': "{:.2f}".format(float("{0:.2f}".format(book.price)) * int(request.POST.get("quantity"))),
            
            # book image url
            'book_image': book.image.cdn_url,
            
            # author
            'authors': authors_list
        }
        
        # save the shopping cart back to session
        request.session['shopping_cart'] = cart
        
        # message to display items successfully added to cart
        messages.success(request, 'Item(s) added to shopping cart!')
    
    return redirect(reverse('get_index'))
    
def remove_from_cart(request, book_id):
    
    # retrieve the cart from session
    cart = request.session.get('shopping_cart',{})
    
    # if the course is in the cart
    if book_id in cart:
        
        # remove it from the cart
        del cart[book_id]
        # save back to the session
        request.session['shopping_cart'] = cart
        
        messages.success(request, "Item(s) successfully removed from shopping cart!")
        
        if len(cart) >= 1: 
            return redirect(reverse('view_cart')) 
        else:
            return redirect(reverse('get_index')) 

def update_cart(request, book_id):

    # get updated quantity
    if ('newqty' in request.GET):
         newQty = int(request.GET.get('newqty'))
    
    # get book id
    if ('bookId' in request.GET):
        book_id = int(request.GET.get('bookId'))
        
    # get row record
    if ('divId' in request.GET):
        div_id = int(request.GET.get('divId'))
    
    # get the relevant book in the shopping cart and update its quantity
    cart = request.session.get('shopping_cart', {})
    
  
    # get the old quantity ordered
    old_quantity_in_cart = cart[str(book_id)]['quantity_ordered']

    # difference between old and new quantity ordered 
    diff_in_quantity = newQty - old_quantity_in_cart
    
    # update quantity available based on cart update
    cart[str(book_id)]['available_quantity'] = cart[str(book_id)]['available_quantity'] - diff_in_quantity
    
    cart[str(book_id)]['quantity_ordered'] = newQty
    
    cart[str(book_id)]['total_price'] = "{:.2f}".format(cart[str(book_id)]['price'] * newQty)
    
    # save the shopping cart back to session
    request.session['shopping_cart'] = cart   
    
    # add in row id record 140220
    cart[str(book_id)]['row_id'] = div_id
    
    shopping_cart = list(cart.values())
    
    # append the total items in the cart to the shopping cart list
    new_total_quantity = 0
    
    for elem in shopping_cart:
        new_total_quantity = (new_total_quantity + int(elem['quantity_ordered']))
        new_total_quantity = new_total_quantity
    
    shopping_cart.append({'new_total_quantity': new_total_quantity})

    return JsonResponse(shopping_cart, safe=False)
