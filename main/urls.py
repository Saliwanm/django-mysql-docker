from django.urls import path
from .views import homeView, sign_upView, sign_inView, logoutView

urlpatterns = [
    path("", homeView, name="home"),
    path("sign-up", sign_upView, name="sign-up"),
    path("sign-in", sign_inView, name="sign-in"),
    path("logout", logoutView, name="logout"),
]