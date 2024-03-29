from django.contrib import admin
from product.models import Category, Product, Review, Tag

# Register your models here.
@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'description')
    list_editable = ('price', 'category')
    search_fields = ('title', 'category', 'tags')
    readonly_fields = ('id',)
    fields = ('title', 'price', 'category', 'description', 'tags')

admin.site.register(Category)
admin.site.register(Review)
admin.site.register(Tag)