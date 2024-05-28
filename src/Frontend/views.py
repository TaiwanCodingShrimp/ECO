from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from Board.forms import BoardForm
from Board.models import Board

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



@login_required
def board_view(request):
    boards = Board.objects.all()
    return render(request, "board.html", {"boards": boards})


@login_required

def organization_view(request):
    return render(request, "organization.html")



@login_required
def report_view(request):
    return render(request, "report.html")


@login_required
def users_view(request):
    return render(request, "users.html")


@login_required
def create_board_view(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user
            board.user_id = request.user
            board.save()
            return redirect("board")
    else:
        form = BoardForm()
    return render(request, "createboard.html", locals())


@login_required
def board_detail_view(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, "boarddetail.html", {"board": board})

