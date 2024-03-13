from django.contrib import admin
from product.models import Category, Product, Review

# Register your models here.
@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'description')
    list_display_links = ('title',)
    list_editable = ('price', 'category')
    list_filter = ('price', 'category')
    search_fields = ('title', 'category')
    readonly_fields = ('id',)
    fields = ('title', 'price', 'category', 'description')

admin.site.register(Category)
admin.site.register(Review)