from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from Board.forms import BoardForm
from Board.models import Board
from Organization.models import Food_Bank, WelfareOrganization
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
def organizations_view(request):
    selected_type = request.GET.get("type", "organization")
    selected_county = request.GET.get("county", "")
    selected_district = request.GET.get("district", "")

    if selected_type == "organization":
        model = WelfareOrganization
    elif selected_type == "food_bank":
        model = Food_Bank
    else:
        model = None

    if model:
        counties = model.objects.values_list("county", flat=True).distinct()
        if selected_county:
            districts = (
                model.objects.filter(county=selected_county)
                .values_list("district", flat=True)
                .distinct()
            )
        else:
            districts = model.objects.values_list("district", flat=True).distinct()

        organizations = model.objects.all()
        if selected_county:
            organizations = organizations.filter(county=selected_county)
        if selected_district:
            organizations = organizations.filter(district=selected_district)
    else:
        counties = []
        districts = []
        organizations = []

    # 將過濾後的數據傳遞給模板
    context = {
        "selected_type": selected_type,
        "counties": counties,
        "districts": districts,
        "organizations": organizations,
        "selected_county": selected_county,
        "selected_district": selected_district,
    }
    return render(request, "organizations.html", context)


@login_required
def report_view(request):
    return render(request, "report.html")


@login_required
def users_view(request):
    users = request.user
    return render(request, "users.html", {"users": users})


@login_required
def create_board_view(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user
            board.save()
            return redirect("board")
    else:
        form = BoardForm()
    return render(request, "createboard.html", locals())


@login_required
def board_detail_view(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, "boarddetail.html", {"board": board})
