from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Review, Category
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer


# Create your views here.
@api_view(['GET'])
def product_list_api_view(request):
    product_list = Product.objects.all()
    data = ProductSerializer(product_list, many=True)
    return Response(data=data.data)

@api_view(['GET'])
def product_detail_api_view(request, id):
    try:
        product_detail = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Product Not Found"})
    data = ProductSerializer(product_detail)
    return Response(data=data.data)


@api_view(['GET'])
def category_list_api_view(request):
    category_list = Category.objects.all()
    data = CategorySerializer(category_list, many=True)
    return Response(data=data.data)

@api_view(['GET'])
def category_detail_api_view(request, id):
    try:
        category_detail = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Category Not Found"})
    data = CategorySerializer(category_detail)
    return Response(data=data.data)


@api_view(['GET'])
def review_list_api_view(request):
    review_list = Review.objects.all()
    data = ReviewSerializer(review_list, many=True)
    return Response(data=data.data)

@api_view(['GET'])
def review_detail_api_view(request, id):
    try:
        review_detail = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Review Not Found"})

    data = ReviewSerializer(review_detail)
    return Response(data=data.data)
