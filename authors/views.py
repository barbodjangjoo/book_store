from django.shortcuts import render
from .models import Author

def author_list_view(request):
    authors = Author.objects.all()
    return render(request, 'authors/author_list.html', {'authors': authors})

