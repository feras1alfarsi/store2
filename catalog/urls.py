from django.urls import path

app_name = "catalog"

urlpatterns = [
    # سيتم إضافة مسارات الكتالوج لاحقاً
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),  # ← home هنا
]
