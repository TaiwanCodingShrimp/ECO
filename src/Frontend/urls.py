from django.urls import path

from .views import home_view, index_view, login_view, logout_view, signup_view

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("home/", home_view, name="home"),
    path("", index_view, name="index"),
]
