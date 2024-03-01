from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MenuItem
from products.models import ProductsModel
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def homeView(request):
    menu_items = MenuItem.objects.all()
    # products = ProductsModel.objects.filter(display_on_main_page=True, approved=True).order_by("-id")
    return render(request, "main/index.html", {
        "menu_items": menu_items,
        # "products": products,
        # "count_cart": len(request.session.get("cart", {"products": [], "total": 0})["products"])
    })

def sign_upView(request):
    if request.method == "POST":
        user = User()
        user.username = request.POST.get("username")
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.email = request.POST.get("email")
        user.set_password(request.POST.get("password"))
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True
        user.save()
        return redirect("/")
    else:
        return render(request, "main/sign-up.html", {})
    
def sign_inView(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))
        print("================USER ===============")
        print(user)
        if user:
            login(request, user)
        return redirect("/")
    else:
        return render(request, "main/sign-in.html", {})


def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/")

def add_to_cart_View(request, id):
    product = ProductsModel.objects.get(id=id)
    if request.session.get("cart", False):
        is_product_already_added = False
        for el in request.session.get("cart", {"products": [], "total": 0})["products"]:
            if el["id"] == id:
                el["count"] = el["count"] + 1
                request.session["cart"]["total"] = request.session["cart"]["total"] + product.price
                el["price"] = el["price"] + product.price
                is_product_already_added = True
        if not is_product_already_added:
            request.session["cart"]["total"] = request.session["cart"]["total"] + product.price
            request.session["cart"]["products"].append({
                "id": product.id,
                "title": product.tittle,
                "price": product.price,
                "count": 1
            })
    else:
        request.session["cart"] = {
            "products": [],
            "total": 0
        }
        request.session["cart"]["total"] = product.price
        request.session["cart"]["products"].append({
            "id": product.id,
            "title": product.tittle,
            "description": product.description,
            "price": product.price,
            "count": 1
        })
    request.session.modified = True
    return redirect("/cart")


def show_cart_View(request):
    return render(request, "main/cart.html", {
        "count_cart": len(request.session.get("cart", {"products": [], "total": 0})["products"]),
        "products": request.session.get("cart", {"products": [], "total": 0})["products"],
        "total": request.session.get("cart", {"products": [], "total": 0})["total"],
    })


def delete_cart_View(request, id):
    if request.session.get("cart", False):
        products = request.session["cart"]["products"]
        for i in range(len(products)):
            print(products[i])
            print(id)
            if products[i]["id"] == int(id):
                request.session["cart"]["total"] = request.session["cart"]["total"] - products[i]["price"]
                del request.session["cart"]["products"][i]
                request.session.modified = True
                break
        return redirect("/cart")