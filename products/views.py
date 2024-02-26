from django.shortcuts import redirect, render, get_object_or_404
from .models import ProductsView


def add_productView(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "products/add_product.html")
        else:
            product = ProductsView()
            product.tittle = request.POST.get("title")
            product.description = request.POST.get("description")
            product.user = request.user
            product.save()
            return redirect("/")
    else:
        return redirect("/")


def product_detail_View(request, id):
    # product = ProductsView.objects.get(id=id)
    product = get_object_or_404(ProductsView, id=id)
    return render(request, "products/details.html", {
        'product': product,
    })