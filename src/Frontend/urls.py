from django.urls import path

from .views import (
    board_detail_view,
    board_view,
    create_board_view,
    donation_view,
    food_bank_view,
    home_view,
    index_view,
    login_view,
    logout_view,
    report_view,
    signup_view,
    users_view,
    welfare_organization_view,
)

urlpatterns = [
    path("signup/", signup_view, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("home/", home_view, name="home"),
    path("", index_view, name="index"),
    path("home/board/", board_view, name="board"),
    path("home/board/createboard/", create_board_view, name="createboard"),
    path("home/board/<int:board_id>/", board_detail_view, name="board_detail"),
    path("home/users/report/", report_view, name="report"),
    path("home/users/WelfareOrganization/", welfare_organization_view, name="welfare"),
    path("home/users/FoodBank", food_bank_view, name="foodbank"),
    path("home/users/donation/", donation_view, name="donation"),
    path("home/users/", users_view, name="users"),
]
