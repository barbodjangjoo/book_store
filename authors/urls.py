from django.urls import path

from . import views

urlpatterns = [
    path('', views.author_list_view, name='author_list'),
    path('<int:pk>/', views.author_detail_view, name='author_detail'),
]
