from django.contrib import admin
from applications.product.models import Product, Category, Image

admin.site.register(Product)
admin.site.register(Category)

