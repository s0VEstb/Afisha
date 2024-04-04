from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from product.models import Category, Product, Review, Tag


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'product', 'text', 'stars']


class ReviewValiditySerializer(serializers.Serializer):
    text = serializers.CharField(min_length=1, max_length=100)
    product = serializers.IntegerField(min_value=1)
    stars = serializers.IntegerField(min_value=1, max_value=5)



class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'tags', 'reviews', "average_rating"]

    def get_average_rating(self, product):
        reviews = product.reviews.all()
        if reviews:
            sum_reviews = sum(i.stars for i in reviews)
            average = sum_reviews / len(reviews)
            return average
        return None


class ProductValiditySerializer(serializers.Serializer):
    title = serializers.CharField(min_length=1, max_length=50)
    description = serializers.CharField(min_length=1, max_length=100, required=False)
    price = serializers.IntegerField(min_value=1)
    category = serializers.IntegerField(min_value=1)
    tags = serializers.ListField(child=serializers.IntegerField(min_value=1), required=False)

    def validate_tags(self, tags):
        tag_a = set(tags)
        tags_db = Tag.objects.filter(id__in=tag_a)
        if len(tags_db) != len(tags):
            raise ValidationError("Tag doesn't exist")
        return tags



class CategorySerializer(serializers.ModelSerializer):
    count_products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['name', 'count_products']

    def get_count_products(self, category):
        count = category.category.count()
        return count

