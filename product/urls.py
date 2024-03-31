from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list_api_view),
    path('products/<int:id>/', views.product_detail_api_view),
    path('category/', views.category_list_api_view),
    path('category/<int:id>/', views.category_detail_api_view),
    path('review/', views.review_list_api_view),
    path('review/<int:id>/', views.review_detail_api_view),
]