from django.urls import path

from . import views

urlpatterns = [
    path('', views.author_list_view, name='author_list'),
]
