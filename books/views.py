from typing import Any
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import mixins
from django.urls import reverse_lazy


from .models import Book, Comment
from .forms import CommentForm

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
    template_name = 'books/book_detail.html'  # Specify the template name

    def form_valid(self, form):
        form.instance.book_id = self.kwargs['pk']
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.kwargs['pk']})