from django import forms

from .models import Author, AuthorComment

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['image', 'name', 'birth_date', 'bio']

class AuthorCommentForm(forms.ModelForm):
    class Meta:
        model = AuthorComment
        fields = ['text']

