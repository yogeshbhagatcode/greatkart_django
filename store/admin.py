from django.contrib import admin
from .models import Product, Variant


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = ['product_name', 'price', 'stock', 'is_available', 'category', 'created_date', 'modified_date']


class VariantAdmin(admin.ModelAdmin):
    list_display = ['product', 'variant_category', 'variant_value', 'is_active']
    list_filter = ['variant_category', 'variant_value']


admin.site.register(Product, ProductAdmin)
admin.site.register(Variant, VariantAdmin)