from django.urls import path

from .views import (
    board_detail_view,
    board_view,
    create_board_view,
    home_view,
    index_view,
    login_view,
    logout_view,
    organizations_view,
    report_view,
    signup_view,
    users_view,
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
    path("home/organizations/", organizations_view, name="organizations"),
    path("home/users/report/", report_view, name="report"),
    path("home/users/", users_view, name="users"),
]
