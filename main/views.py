from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MenuItem
from products.models import ProductsView
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def homeView(request):
    menu_items = MenuItem.objects.all()
    products = ProductsView.objects.filter(Q(dysplay_on_main_page=True) | Q(approved=True)).order_by("-tittle")
    return render(request, "main/index.html", {
        "menu_items": menu_items,
        "products": products,
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