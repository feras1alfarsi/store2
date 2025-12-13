from django.contrib import admin
from .models import CustomUser, SiteSettings
from django.contrib.auth.admin import UserAdmin


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    تسجيل المستخدم المخصص مع الحقول الإضافية.
    """
    fieldsets = UserAdmin.fieldsets + (
        ('معلومات إضافية', {'fields': ('phone', 'city')}),
    )

    list_display = ('username', 'email', 'phone', 'city', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'phone', 'city')


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'contact_email', 'contact_phone', 'updated_at')
    search_fields = ('store_name',)
