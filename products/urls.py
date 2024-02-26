from django.urls import path
from .views import add_productView, product_detail_View

urlpatterns = [
    path("/add", add_productView, name="add_product"),
    path("/<int:id>", product_detail_View, name="product_details"),
]