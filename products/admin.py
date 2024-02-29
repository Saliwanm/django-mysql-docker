from django.contrib import admin

from .models import ProductsModel, CategoryModel, CategoryProductModel


admin.site.register(ProductsModel)
admin.site.register(CategoryModel)
admin.site.register(CategoryProductModel)
