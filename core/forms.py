from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import re

User = get_user_model()


class SignupForm(forms.ModelForm):
    password1 = forms.CharField(
        label="كلمة المرور",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        label="تأكيد كلمة المرور",
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ["username", "email", "phone"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
        }

    # =========================
    # التحقق من التفرد
    # =========================
    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError("اسم المستخدم مستخدم مسبقًا")
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("البريد الإلكتروني مستخدم مسبقًا")
        return email

    def clean_phone(self):
        phone = self.cleaned_data["phone"]
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
            raise ValidationError("يجب أن تحتوي على حرف كبير")

        if not re.search(r"[a-z]", password):
            raise ValidationError("يجب أن تحتوي على حرف صغير")

        if not re.search(r"[0-9]", password):
            raise ValidationError("يجب أن تحتوي على رقم")

        if not re.search(r"[!@#$%^&*()_+=\-]", password):
            raise ValidationError("يجب أن تحتوي على رمز")

        return password

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")

        if p1 and p2 and p1 != p2:
            raise ValidationError("كلمتا المرور غير متطابقتين")

        return cleaned_data

    # =========================
    # حفظ المستخدم
    # =========================
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
