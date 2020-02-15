def cart_contents(request):
    # make the content of the shopping cart available to all templates
    cart = request.session.get("shopping_cart", {})
    
    # loop through all the cart items and sum up all the items in the cart
    cart_item = 0
    if len(cart) == 0:
        cart_item = cart_item
    else:
        for key in cart:
            cart_item = cart_item + cart[key]['quantity_ordered']
        
    # 130220
    rows_of_record = len(cart)
    
    # save the cart_item to session object
    request.session['total_qty_in_cart'] = cart_item
    
    return {
        'shopping_cart':cart,
        'number_of_items':cart_item,
        # 130220
        'row_of_record': rows_of_record
    }
