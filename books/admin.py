from django.contrib import admin

from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['title', 'author', 'datetime_created']
