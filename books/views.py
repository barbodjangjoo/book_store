from typing import Any
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.contrib import messages


from .models import Book, Comment
from .forms import CommentForm
from cart.forms import AddToCartBookForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments_form'] = CommentForm()
        context['comments'] = Comment.objects.filter(book=self.object)
        return context

class CommentCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'books/book_detail.html'

    def form_valid(self, form):
        form.instance.book_id = self.kwargs['pk']
        form.instance.user_id = self.request.user.id
        response = super().form_valid(form)
        messages.success(self.request, 'Comment added successfully!')
        return response

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.kwargs['pk']})
    
class BookUpdateView(mixins.LoginRequiredMixin, generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'price', 'short_description', 'description', 'is_active', 'image',]
    template_name = 'books/book_new.html'

class BookAddView(mixins.LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = ['title', 'author', 'price', 'short_description', 'description', 'is_active', 'image',]
    template_name = 'books/book_new.html'
    
    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.object.id})
    
class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
