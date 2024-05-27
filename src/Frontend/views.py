from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from Users.forms import LoginForm, SignUpForm


def index_view(request):
    return render(request, "index.html")


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")


@login_required
def home_view(request):
    user = request.user
    username = user.email
    return render(request, "home.html", locals())


def board_view(request):
    return render(request, "board.html")


def organization_view(request):
    return render(request, "organization.html")


def report_view(request):
    return render(request, "report.html")


def users_view(request):
    return render(request, "users.html")
