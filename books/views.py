from typing import Any
from django.shortcuts import render
from django.views import generic

from .models import Book

class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name= 'books'

    def get_queryset(self):
        return Book.objects.filter(is_active = True)

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'