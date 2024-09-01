from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book

def home(request):
    return render(request, 'home.html')

def book_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book': book})

class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'date_of_publication', 'ISBN']
    success_url = '/books/'

class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author', 'date_of_publication', 'ISBN']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'