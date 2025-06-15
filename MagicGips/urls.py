from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='products'),
    path('products/', views.products, name='products'),
    path('products/<str:product_name>/', views.product_detail, name='product_detail'),
]