from django.contrib import admin

from .models import Author, AuthorComment

admin.site.register(Author)
admin.site.register(AuthorComment)

# Register your models here.
