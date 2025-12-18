from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية + تسجيل الدخول + التسجيل
    path('', include('core.urls')),

    # التطبيقات الأخرى
    path('catalog/', include('catalog.urls')),
    path('shop/', include('shop.urls')),
]

# خدمة ملفات media أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
