from django.contrib import admin

from .models import Product, Specification, ProductImage

admin.site.register(Product)
admin.site.register(Specification)
admin.site.register(ProductImage)