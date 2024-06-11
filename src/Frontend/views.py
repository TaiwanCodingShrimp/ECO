from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from Board.forms import BoardForm
from Board.models import Board
from Organization.models import Food_Bank, WelfareOrganization
from Users.forms import FootPrintForm, LeftoverForm, LoginForm, SignUpForm, WasteForm
from Users.models import FootPrint, Leftover, Waste


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


@login_required
def donation_view(request):
    waste_form = WasteForm()
    leftover_form = LeftoverForm()

    if request.method == "POST":
        if "waste_form" in request.POST:
            waste_form = WasteForm(request.POST)
            if waste_form.is_valid():
                waste_form.save()
                return redirect("donation")
        elif "leftover_form" in request.POST:
            leftover_form = LeftoverForm(request.POST)
            if leftover_form.is_valid():
                leftover_form.save()
                return redirect("donation")

    wastes = Waste.objects.all()
    leftovers = Leftover.objects.all()

    context = {
        "waste_form": waste_form,
        "leftover_form": leftover_form,
        "wastes": wastes,
        "leftovers": leftovers,
    }
    return render(request, "donation.html", context)


def welfare_organization_view(request):
    selected_county = request.GET.get("county", "")
    selected_district = request.GET.get("district", "")

    counties = WelfareOrganization.objects.values_list("county", flat=True).distinct()
    if selected_county:
        districts = (
            WelfareOrganization.objects.filter(county=selected_county)
            .values_list("district", flat=True)
            .distinct()
        )
    else:
        districts = WelfareOrganization.objects.values_list(
            "district", flat=True
        ).distinct()

    organizations = WelfareOrganization.objects.all()
    if selected_county:
        organizations = organizations.filter(county=selected_county)
    if selected_district:
        organizations = organizations.filter(district=selected_district)

    context = {
        "selected_county": selected_county,
        "selected_district": selected_district,
        "counties": counties,
        "districts": districts,
        "organizations": organizations,
    }
    return render(request, "welfare.html", context)


def food_bank_view(request):
    selected_county = request.GET.get("county", "")
    selected_district = request.GET.get("district", "")

    counties = Food_Bank.objects.values_list("county", flat=True).distinct()
    if selected_county:
        districts = (
            Food_Bank.objects.filter(county=selected_county)
            .values_list("district", flat=True)
            .distinct()
        )
    else:
        districts = Food_Bank.objects.values_list("district", flat=True).distinct()

    organizations = Food_Bank.objects.all()
    if selected_county:
        organizations = organizations.filter(county=selected_county)
    if selected_district:
        organizations = organizations.filter(district=selected_district)

    context = {
        "selected_county": selected_county,
        "selected_district": selected_district,
        "counties": counties,
        "districts": districts,
        "organizations": organizations,
    }
    return render(request, "foodbank.html", context)


@login_required
def footprint_view(request):
    form = FootPrintForm()
    if request.method == "POST":
        form = FootPrintForm(request.POST)
        if form.is_valid():
            footprint = form.save(commit=False)
            footprint.users_id = request.user
            footprint.save()
            return redirect("footprint")  # Redirect to the same page after saving
        else:
            return redirect("footprint")
    else:
        form = FootPrintForm()

    footprints = FootPrint.objects.filter(users_id=request.user)

    return render(request, "footprint.html", {"form": form, "footprints": footprints})
