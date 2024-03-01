from django.urls import path
from .views import homeView, logoutView, sign_inView, sign_upView, add_to_cart_View, show_cart_View, delete_cart_View
# from .views import homeView, sign_upView, sign_inView, logoutView, add_to_cart_View, show_cart_View, delete_cart_View

urlpatterns = [
    path("", homeView, name="home"),
    path("sign-up", sign_upView, name="sign-up"),
    path("sign-in", sign_inView, name="sign-in"),
    path("logout", logoutView, name="logout"),
    path("cart/<int:id>", add_to_cart_View, name="add_to_cart"),
    path("cart", show_cart_View, name="show_cart"),
    path("cart/delete/<int:id>", delete_cart_View, name="delete_cart"),
]