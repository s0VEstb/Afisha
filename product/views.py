from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Review, Category
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        product_list = Product.objects.prefetch_related('reviews').all()
        data = ProductSerializer(product_list, many=True)
        return Response(data=data.data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category')
        Product.objects.create(title=title, description=description, price=price, category_id=category_id)

        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product_detail = Product.objects.get(id=id)
        print(product_detail.category)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Product Not Found"})
    if request.method == 'GET':
        data = ProductSerializer(product_detail)
        return Response(data=data.data)
    elif request.method == 'PUT':
        product_detail.title = request.data.get('title')
        product_detail.description = request.data.get('description')
        product_detail.price = request.data.get('price')
        product_detail.category_id = request.data.get('category')
        product_detail.save()
        return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        product_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    if request.method == 'GET':
        category_list = Category.objects.all()
        data = CategorySerializer(category_list, many=True)
        return Response(data=data.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        Category.objects.create(name=name)
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', "DELETE"])
def category_detail_api_view(request, id):
    try:
        category_detail = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Category Not Found"})
    if request.method == 'GET':
        data = CategorySerializer(category_detail)
        return Response(data=data.data)
    elif request.method == 'PUT':
        category_detail.name = request.data.get('name')
        category_detail.save()
        return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        category_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        review_list = Review.objects.all()
        data = ReviewSerializer(review_list, many=True)
        return Response(data=data.data)
    elif request.method == 'POST':
        text = request.data.get('text')
        product_id = request.data.get('product')
        stars = request.data.get('stars')
        Review.objects.create(product_id=product_id, stars=stars, text=text)
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review_detail = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Review Not Found"})
    if request.method == 'GET':
        data = ReviewSerializer(review_detail)
        return Response(data=data.data)
    elif request.method == 'PUT':
        review_detail.text = request.data.get('text')
        review_detail.product_id = request.data.get('product')
        review_detail.stars = request.data.get('stars')
        review_detail.save()
        return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
