from django.urls import path

from . import views

urlpatterns = [
    path('', views.cart_detail_view, name='cart_detail'),
    path('add/<int:book_id>/', views.add_to_cart_view, name='cart_add'),
    path('remove/<int:book_id>/', views.remove_cart, name='cart_remove'),

]
