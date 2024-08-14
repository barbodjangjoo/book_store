from django.contrib import admin

from .models import Book, Comment

class CommentInline(admin.TabularInline):
    model= Comment
    fields = ['user', 'text', ]
    extra = 0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ['title', 'author', 'datetime_created']
    inlines= [
        CommentInline,
    ]
