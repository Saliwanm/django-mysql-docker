from django.urls import path
from .views import productsView, product_detail_View, edit_product_View, add_productView, update_product_View
# from .views import add_productView, product_detail_View, edit_product_View, productsView, update_product_View, add_categoryView

urlpatterns = [
    path("add", add_productView, name="add_product"),
    path("", productsView, name="products"),
    path("edit/<int:id>", edit_product_View, name="edit_product"),
    path("update/<int:id>", update_product_View, name="update_product"),
    path("<int:id>", product_detail_View, name="product_details"),
    # path("category/add", add_categoryView, name="add_category"),
]