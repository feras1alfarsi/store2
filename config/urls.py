from django.contrib import admin
from django.urls import path, include  # إضافة include لربط التطبيقات

urlpatterns = [
    path('admin/', admin.site.urls),

    # مسارات التطبيقات الجديدة
    path('', include('core.urls')),          # الصفحة الرئيسية + صفحات ثابتة
    path('catalog/', include('catalog.urls')),  # المنتجات والتصنيفات
    path('shop/', include('shop.urls')),       # السلة والطلبات والدفع
]
