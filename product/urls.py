from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListAPIView.as_view()),
    path('products/<int:id>/', views.ProductDetailAPIView.as_view()),
    path('category/', views.CategoryListAPIView.as_view()),
    path('category/<int:id>/', views.CategoryDetailAPIView.as_view()),
    path('review/', views.ReviewListAPIView.as_view()),
    path('review/<int:id>/', views.ReviewDetailAPIView.as_view()),
]