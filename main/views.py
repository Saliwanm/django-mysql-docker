from django.shortcuts import render
from django.http import HttpResponse
from .models import MenuItem
from products.models import ProductsView
from django.db.models import Q


def homeView(request):
    menu_items = MenuItem.objects.all()
    products = ProductsView.objects.filter(Q(dysplay_on_main_page=True) | Q(approved=True)).order_by("-tittle")
    return render(request, "main/index.html", {
        "menu_items": menu_items,
        "products": products,
    })