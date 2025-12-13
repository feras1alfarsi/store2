from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح سري للتطوير فقط — يجب تغييره في بيئة الإنتاج
SECRET_KEY = 'django-insecure-@r053ri(8g2m&*--td(uo-d7b3be1%fw&_8n*b^0)i(6+i59r@'

DEBUG = True

# أضف النطاقات المسموح بها عند تشغيل المشروع عبر الإنترنت
ALLOWED_HOSTS = []


# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # التطبيقات الخاصة بالمتجر
    'core',
    'catalog',
    'shop',
]

AUTH_USER_MODEL = "core.CustomUser"


# ميدلوير
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    # دعم اللغة العربية
    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'


# القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # إضافة مجلد قوالب
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',  # دعم اللغة
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# قواعد كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# اللغة – العربية
LANGUAGE_CODE = 'ar'

# المنطقة الزمنية – الرياض
TIME_ZONE = 'Asia/Riyadh'

USE_I18N = True
USE_TZ = True


# الملفات الثابتة
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# دعم ملفات الترجمة (لمن يريد عمل تعدد لغات مستقبلاً)
LOCALE_PATHS = [
    BASE_DIR / "locale"
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

