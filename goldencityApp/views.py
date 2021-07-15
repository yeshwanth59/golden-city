from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Master
from .forms import RegistrationForm, LoginForm
# Create your views here.


def home(request):
    img = Master.objects.all()
    return render(request, "home.html", {"img": img})


def reg(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Registration completed successfully")
    else:
        form = RegistrationForm()
        return render(request, "reg.html", {"form": form})


def login(request):
    if request.method == "POST":
        my_loginform = LoginForm(request.POST)
        if my_loginform.is_valid():
            un = my_loginform.cleaned_data['username']
            pwd = my_loginform.cleaned_data['password']
            dbuser = User.objects.filter(username=un, password=pwd)

            if not dbuser:
                return HttpResponse("Login Failed ")
            else:
                return HttpResponse("Login successfully ")
    else:
        my_form = LoginForm()
        return render(request, "login.html", {"my_form": my_form})


def contact(request):
    return render(request, "contact_us.html")

#
# def mbnr(request):
#     img = Master.objects.all()
#     return render(request, "mbnr.html", {"img": img})