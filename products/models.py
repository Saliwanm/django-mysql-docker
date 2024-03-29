from django.db import models

from django.contrib.auth.models import User


class ProductsModel(models.Model):
    tittle = models.CharField(max_length=255)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField()
    approved_by = models.ForeignKey(User, related_name="approved_by", null=True, on_delete=models.SET_NULL)
    approved = models.BooleanField(default=False)
    dysplay_on_main_page = models.BooleanField(default=False)

    def __str__(self):
        return self.tittle


class CategoryModel(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class CategoryProductModel(models.Model):
    product = models.ForeignKey(ProductsModel, on_delete=models.PROTECT)
    category = models.ForeignKey(CategoryModel, on_delete=models.PROTECT)

    def __str__(self):
        return self.category.title + "-------" + self.product.tittle