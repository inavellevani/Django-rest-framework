from django.urls import path
from .views import (
    ProductCreateView,
    ProductDetailView,
    ProductListView,
    ProductDeleteView,
    ProductUpdateView,
    CategoryListView,
)

urlpatterns = [
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]