from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('books/', views.book_index, name='book-index'),
    path('books/<int:book_id>/', views.book_detail, name='book-detail'),
    path('books/create', views.BookCreate.as_view(), name='book-create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
    path('books/<int:book_id>/add-page/', views.add_page, name='add-page'),
    path('accounts/signup/', views.signup, name='signup'),
]