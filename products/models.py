from django.db import models

from django.contrib.auth.models import User


class ProductsView(models.Model):
    tittle = models.CharField(max_length=255)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    description = models.TextField()
    approved_by = models.ForeignKey(User, related_name="approved_by", null=True, on_delete=models.SET_NULL)
    approved = models.BooleanField(default=False)
    dysplay_on_main_page = models.BooleanField(default=False)

    def __str__(self):
        return self.tittle