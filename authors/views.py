from django.shortcuts import render, get_object_or_404 , redirect
from django.views import generic

from .models import Author
from .forms import AuthorForm


def author_list_view(request):
    authors = Author.objects.all()
    return render(request, 'authors/author_list.html', {'authors': authors})

def author_detail_view(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'authors/author_detail.html', {'author': author})

def author_create_view(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AuthorForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'authors/author_form.html', {'form': form})