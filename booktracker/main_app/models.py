from django.db import models
from isbn_field import ISBNField
from django.urls import reverse

class Book(models.Model):
    title = models.CharField(max_length=1000)
    author = models.CharField(max_length=1000)
    date_of_publication = models.DateField('Publication Date')
    ISBN = ISBNField()

    def __str__(self):
        return f'{self.title} by {self.author}'
    
    def get_absolute_url(self):
        return reverse("book-detail", kwargs={'book_id': self.id})

