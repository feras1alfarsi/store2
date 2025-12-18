from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية
    path('', include('core.urls')),

    # التطبيقات
    path('catalog/', include('catalog.urls')),
    path('shop/', include('shop.urls')),
]
