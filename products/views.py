from django.shortcuts import redirect, render, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.db.models import Q

from .models import ProductsModel, CategoryModel, CategoryProductModel
from .forms import ProductForm



def productsView(request):
    # products = ProductsModel.objects.all()
    products = ProductsModel.objects.filter(Q(dysplay_on_main_page=True) | Q(approved=True)).order_by("-tittle")
    return render(request, "products/products.html", {
        "products": products,
    })


def product_detail_View(request, id):
    # product = ProductsModel.objects.get(id=id)
    product = get_object_or_404(ProductsModel, id=id)
    return render(request, "products/details.html", {
        'product': product,
    })


def add_productView(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            form = ProductForm(initial={
                "user": request.user
            })
            return render(request, "products/add_product.html", {
                "form": form,
            })
        else:
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save(user=request.user)
                return redirect("/")
            else:
                return render(request, "products/add_product.html", {
                    "form": form,
                })
    else:
        return redirect("/")
# def add_productView(request):
#     if request.user.is_authenticated:
#         if request.method == "GET":
#             categories = CategoryModel.objects.all()
#             return render(request, "products/add_product.html", {
#                 "categories": categories,
#             })
#         else:
#             product = ProductsModel()
#             product.tittle = request.POST.get("tittle")
#             product.description = request.POST.get("description")
#             product.user = request.user
#             product.save()
#             return redirect("/")
#     else:
#         return redirect("/")


def edit_product_View(request, id):
    if request.user.is_authenticated:
        product = ProductsModel.objects.get(id=id)
        categories = CategoryModel.objects.all()
        product_categories = CategoryProductModel.objects.filter(product_id=product.id)
        return render(request, "products/add_product.html", {
            "product": product,
            "product_categories": product_categories,
            "categories": categories,
            })
    else:
        raise PermissionDenied


def update_product_View(request, id):
    if request.user.is_authenticated:
        product = ProductsModel.objects.get(id=id)
        product.tittle = request.POST.get("tittle")
        product.description = request.POST.get("description")
        product.save()
        CategoryProductModel.objects.filter(product_id=product.id).delete()
        for category in request.POST.getlist("categories", []):
                category_product = CategoryProductModel()
                category_product.product = product
                category_product.category = CategoryModel.objects.get(id=int(category))
                category_product.save()
        return redirect("/")
    else:
        raise PermissionDenied


def add_categoryView(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "products/add_category.html")
        else:
            category = CategoryModel()
            category.title = request.POST.get("title")
            category.save()
            return redirect("/")