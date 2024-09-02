from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Book, Page
from .forms import PageForm

def home(request):
    return render(request, 'home.html')

def book_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    page_form = PageForm()
    return render(request, 'books/detail.html', {'book': book, 'page_form': page_form})

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

class PageCreate(CreateView):
    model = Page
    fields = '__all__'

class PageList(ListView):
    model = Page

class PageDetail(DetailView):
    model = Page