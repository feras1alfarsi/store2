from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages

from catalog.models import Product
from .forms import SignupForm

User = get_user_model()


# =========================
# الصفحة الرئيسية
# =========================
def home(request):
    products = Product.objects.filter(is_active=True)
    return render(request, "home.html", {
        "products": products
    })


# =========================
# إنشاء حساب جديد
# =========================
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)  # تسجيل دخول تلقائي
            messages.success(request, "تم إنشاء الحساب بنجاح")
            return redirect("home")  # ✅ انتقال فوري للرئيسية
        else:
            messages.error(request, "يرجى تصحيح الأخطاء أدناه")

    else:
        form = SignupForm()

    return render(request, "core-templates/signup.html", {
        "form": form
    })


# =========================
# تسجيل الدخول
# (اسم مستخدم / بريد / جوال)
# =========================
def user_login(request):
    if request.method == "POST":
        identifier = request.POST.get("identifier", "").strip()
        password = request.POST.get("password", "").strip()

        if not identifier or not password:
            messages.error(request, "يرجى إدخال جميع الحقول")
            return redirect("login")

        user = None

        # 1️⃣ اسم المستخدم
        user = authenticate(
            request,
            username=identifier,
            password=password
        )

        # 2️⃣ البريد الإلكتروني
        if user is None:
            try:
                user_obj = User.objects.get(email=identifier)
                user = authenticate(
                    request,
                    username=user_obj.username,
                    password=password
                )
            except User.DoesNotExist:
                pass

        # 3️⃣ رقم الجوال
        if user is None:
            try:
                user_obj = User.objects.get(phone=identifier)
                user = authenticate(
                    request,
                    username=user_obj.username,
                    password=password
                )
            except User.DoesNotExist:
                pass

        if user is not None:
            login(request, user)
            messages.success(request, "تم تسجيل الدخول بنجاح")
            return redirect("home")

        messages.error(request, "بيانات تسجيل الدخول غير صحيحة")

    return render(request, "core-templates/login.html")


# =========================
# تسجيل الخروج
# =========================
def user_logout(request):
    logout(request)
    messages.success(request, "تم تسجيل الخروج")
    return redirect("home")
