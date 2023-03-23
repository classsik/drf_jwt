from django.urls import path

from . import views

urlpatterns = [
    path('books', views.get_books, name='books'),
    path('books/create', views.create_book, name='create_book'),
    path('books/<int:pk>/edit', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete', views.delete_book, name='delete_book'),
    path('books/<int:book_id>/add_to_ordered', views.add_to_ordered, name='add_to_ordered'),
]
