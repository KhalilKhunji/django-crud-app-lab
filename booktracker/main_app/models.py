from django.db import models
from isbn_field import ISBNField
from django.urls import reverse
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    date_of_publication = models.DateField('Publication Date')
    ISBN = ISBNField()
    user = models.ForeignKey (User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def get_absolute_url(self):
        return reverse("book-detail", kwargs={'book_id': self.id})

class Page(models.Model):
    # The Page number is Charfield because some pages are not integers but alphabetical, or use Roman numerals, etc.
    number = models.CharField(max_length=999999)
    content = models.CharField(max_length=1000)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'Page {self.number} containing {self.content}'
    
    class Meta:
        ordering = ['number']