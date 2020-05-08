from django.contrib import admin
from .models import Product, ProductImage
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'update'
    search_fields = ['title', 'description', 'price']
    list_display = ['title', 'price', 'active', 'update']
    list_editable = ['price', 'active']
    list_filter = ['active', 'price']
    readonly_fields = ['update', 'timestamp']
    prepopulated_fields = {'slug':('title', )}
    class Meta:
        model = Product




admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage) 
