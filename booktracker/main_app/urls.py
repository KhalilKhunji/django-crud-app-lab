from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_index, name='book-index'),
    path('books/<int:book_id>/', views.book_detail, name='book-detail')
]