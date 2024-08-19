from django.db import models
from django.urls import reverse

class Author(models.Model):
    image = models.ImageField(upload_to='authors/authors_cover')
    name = models.CharField(max_length=100)
    birth_date = models.DateTimeField()

    bio = models.TextField()


