from django.db import models
from django.urls import reverse

class Author(models.Model):
    image = models.ImageField(upload_to='authors/authors_cover')
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    bio = models.TextField()
    
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


