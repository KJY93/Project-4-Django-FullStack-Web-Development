from django.db import models
from Accounts.models import NewUser

from Catalog.models import Book

# 230220
from decimal import Decimal

class Charge(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)
        
class Order(models.Model):
    STATUS_CHOICES = (
        ('processing', 'Processing'),
        ('dispatched', 'Dispatched'),
        ('delivered', 'Delivered')
    )
    
    customer = models.ForeignKey(NewUser, on_delete=models.SET_NULL, null=True)
    stripe_token = models.CharField(max_length=256)
    status = models.CharField(choices=STATUS_CHOICES, default='Processing', max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def total_cost(self):
        return '{0:.2f}'.format(sum(item.get_cost() for item in self.items.all()))
        
    def delivery_cost(self):
        if Decimal(self.total_cost()) > Decimal(100.00):
            return '{0:.2f}'.format(0)
        else:
            return '{0:.2f}'.format(3.95)  
            
    def subtotal_cost(self):
        return '{0:.2f}'.format(Decimal(self.total_cost()) + Decimal(self.delivery_cost()))

    def __str__(self):
        return f"{self.customer}"
        

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(Book, related_name='order_items', on_delete=models.CASCADE)
    
    def get_cost(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f"Customer: {self.order} - Product: {self.product} - Quantity: {self.quantity} - Price: ${self.price}"



