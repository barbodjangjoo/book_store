from django.urls import path

from . import views
urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('add/', views.BookAddView.as_view(), name= 'book_add'),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name="book_delete"),
    path('<int:pk>/commentcreat/', views.CommentCreateView.as_view(), name='comment_create'),

]
