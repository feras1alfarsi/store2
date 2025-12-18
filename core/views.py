from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from catalog.models import Product
from .forms import SignupForm

User = get_user_model()


def home(request):
    products = Product.objects.filter(is_active=True)
    return render(request, "home.html", {"products": products})


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "تم إنشاء الحساب بنجاح")
            return redirect("home")
    else:
        form = SignupForm()

    return render(request, "shop-templates/signup.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        identifier = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=identifier, password=password)

        if user:
            login(request, user)
            return redirect("home")

        messages.error(request, "بيانات تسجيل الدخول غير صحيحة")

    return render(request, "shop-templates/login.html")


def user_logout(request):
    logout(request)
    return redirect("home")
