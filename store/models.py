from django.db import models
from category.models import Category
from django.urls import reverse


class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=2000, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse ('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


class VariantManager(models.Manager):
    def color(self):
        return super(VariantManager, self).filter(variant_category='color', is_active=True)
    
    def size(self):
        return super(VariantManager, self).filter(variant_category='size', is_active=True)


variant_category_choices = (
    ('color', 'Color'),
    ('size', 'Size'),
)

class Variant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant_category = models.CharField(max_length=150, choices=variant_category_choices)
    variant_value = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)

    objects = VariantManager()

    def __unicode__(self):
        return self.product