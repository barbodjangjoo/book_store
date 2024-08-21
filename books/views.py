from typing import Any
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import mixins
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _


from .models import Book, Comment
from .forms import CommentForm
from cart.forms import AddToCartBookForm

# List view to display all active books
class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name= 'books'
    paginate_by = 4

    # Override get_queryset to only show active books  
    def get_queryset(self):
        return Book.objects.filter(is_active = True)

# Detail view to display a single book
class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

    # Add comment form and comments to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments_form'] = CommentForm()
        context['comments'] = Comment.objects.filter(book=self.object)
        return context

# Create view to add a new comment
class CommentCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'books/book_detail.html'

    # Set the book and user IDs on the comment form
    def form_valid(self, form):
        form.instance.book_id = self.kwargs['pk']
        form.instance.user_id = self.request.user.id
        response = super().form_valid(form)
        messages.success(self.request, _('Comment added successfully!'))
        return response
        
    # Redirect to the book detail page after creating a comment
    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.kwargs['pk']})
    
 # Update view to edit an existing book
class BookUpdateView(mixins.LoginRequiredMixin, generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'price', 'description', 'is_active', 'image',]
    template_name = 'books/book_new.html'

# Create view to add a new book
class BookAddView(mixins.LoginRequiredMixin, generic.CreateView):
    model = Book
    fields = ['title', 'author', 'price', 'description', 'is_active', 'image',]
    template_name = 'books/book_new.html'
    
    # Redirect to the book detail page after creating a new book
    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.object.id})
    
# Delete view to delete a book
class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
