from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator

from pyuploadcare.dj.models import ImageField

class Genre(models.Model):
    
    category_description = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)', unique=True)
    
    def __str__(self):
        """String for representing the Model object."""
        return self.category_description
        
class Author(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):

    title = models.CharField(max_length=255, blank=False)
    author = models.ManyToManyField(Author, help_text='Select an author.')
    publisher = models.CharField(max_length=255, blank=False)
    quantity = models.IntegerField(blank=False, validators=[MinValueValidator(0)])
    pages = models.IntegerField(blank=False, validators=[MinValueValidator(0)]) 
    ISBN = models.CharField(max_length=20, blank=False)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book.')
    description = models.TextField(blank=False)
    publishing_year = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text='Price in SGD', validators=[MinValueValidator(Decimal(0.00))])
    image = ImageField(null=True)

    class Meta:
        verbose_name = 'Catalog'
        verbose_name_plural = 'Catalogues'
        
    unique_together = ('title', 'author', 'publisher')
     
    def __str__(self):
        return f"{self.title}"
        
        
