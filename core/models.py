from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    نموذج مستخدم مخصص قابل للتوسّع.
    يمكن لاحقاً إضافة حقول مثل رقم الجوال أو العنوان.
    """
    phone = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username


class SiteSettings(models.Model):
    """
    إعدادات عامة للموقع (اسم المتجر – الشعار – معلومات التواصل).
    """
    store_name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='settings/', blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.store_name
