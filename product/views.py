from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Review, Category
from product.serializers import (ProductSerializer, CategorySerializer, ReviewSerializer,
                                 ProductValiditySerializer, CategoryValiditySerializer, ReviewValiditySerializer)


# Create your views here.
@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == 'GET':
        product_list = Product.objects.prefetch_related('reviews').all()
        data = ProductSerializer(product_list, many=True)
        return Response(data=data.data)
    elif request.method == 'POST':
        validator = ProductValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': validator.errors})

        title = validator.validated_data['title']
        description = validator.validated_data['description']
        price = validator.validated_data['price']
        category_id = validator.validated_data['category']
        # TODO Show a teacher,
        #  reviews = validator.validated_data['reviews']
        #  average_rating = validator.validated_data['average_rating']
        Product.objects.create(title=title, description=description, price=price, category_id=category_id)

        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api_view(request, id):
    try:
        product_detail = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "Product Not Found"})

    if request.method == 'GET':
        data = ProductSerializer(product_detail)
        return Response(data=data.data)

    elif request.method == 'PUT':
        validator = ProductValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': validator.errors})

        product_detail.title = validator.validated_data['title']
        product_detail.description = validator.validated_data['description']
        product_detail.price = validator.validated_data['price']
        product_detail.category_id = validator.validated_data['category']
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
        validator = CategoryValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': validator.errors})

        name = validator.validated_data['name']
        #TODO Show a teacher, count_products = validator.validated_data['count_products']
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
        validator = CategoryValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': validator.errors})

        category_detail.name = validator.validated_data['name']
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
        validator = ReviewValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': validator.errors})

        text = validator.validated_data['text']
        product_id = validator.validated_data['product']
        stars = validator.validated_data['stars']
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
        validator = ReviewValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': validator.errors})

        review_detail.text = validator.validated_data['text']
        review_detail.product_id = validator.validated_data['product']
        review_detail.stars = validator.validated_data['stars']
        review_detail.save()
        return Response(status=status.HTTP_201_CREATED)

    elif request.method == 'DELETE':
        review_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
