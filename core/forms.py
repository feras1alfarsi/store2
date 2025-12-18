from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import re

User = get_user_model()


class SignupForm(forms.ModelForm):
    """
    نموذج إنشاء حساب جديد
    """

    password1 = forms.CharField(
        label="كلمة المرور",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "********"
        })
    )

    password2 = forms.CharField(
        label="تأكيد كلمة المرور",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "********"
        })
    )

    class Meta:
        model = User
        fields = ["username", "email", "phone"]
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "اسم المستخدم"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "example@mail.com"
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "05xxxxxxxx"
            }),
        }

    # =========================
    # التحقق من اسم المستخدم
    # =========================
    def clean_username(self):
        username = self.cleaned_data.get("username")

        if User.objects.filter(username=username).exists():
            raise ValidationError("اسم المستخدم مستخدم مسبقًا")

        return username

    # =========================
    # التحقق من البريد الإلكتروني
    # =========================
    def clean_email(self):
        email = self.cleaned_data.get("email")

        if not email:
            raise ValidationError("البريد الإلكتروني مطلوب")

        if User.objects.filter(email=email).exists():
            raise ValidationError("البريد الإلكتروني مستخدم مسبقًا")

        return email

    # =========================
    # التحقق من رقم الجوال
    # =========================
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")

        if phone:
            if not re.match(r"^05\d{8}$", phone):
                raise ValidationError("رقم الجوال يجب أن يبدأ بـ 05 ويتكون من 10 أرقام")

            if User.objects.filter(phone=phone).exists():
                raise ValidationError("رقم الجوال مستخدم مسبقًا")

        return phone

    # =========================
    # التحقق من قوة كلمة المرور
    # =========================
    def clean_password1(self):
        password = self.cleaned_data.get("password1")

        if len(password) < 8:
            raise ValidationError("كلمة المرور يجب أن تكون 8 أحرف على الأقل")

        if not re.search(r"[A-Z]", password):
            raise ValidationError("يجب أن تحتوي كلمة المرور على حرف كبير")

        if not re.search(r"[a-z]", password):
            raise ValidationError("يجب أن تحتوي كلمة المرور على حرف صغير")

        if not re.search(r"\d", password):
            raise ValidationError("يجب أن تحتوي كلمة المرور على رقم")

        if not re.search(r"[!@#$%^&*()_+=\-]", password):
            raise ValidationError("يجب أن تحتوي كلمة المرور على رمز")

        return password

    # =========================
    # التحقق من تطابق كلمتي المرور
    # =========================
    def clean(self):
        cleaned_data = super().clean()

        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("كلمتا المرور غير متطابقتين")

        return cleaned_data

    # =========================
    # حفظ المستخدم بشكل صحيح
    # =========================
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

        return user
