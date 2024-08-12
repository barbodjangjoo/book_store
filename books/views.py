from django.shortcuts import render
from django.views import generic

from .models import Book

class Home(generic.TemplateView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name= 'books'
