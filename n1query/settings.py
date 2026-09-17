import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-n1-query-learning-project")
DEBUG = os.environ.get("DEBUG", "True").lower() in ("true", "1", "t")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",") if os.environ.get("ALLOWED_HOSTS") else ["*"]

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core.apps.CoreConfig",
]

JAZZMIN_SETTINGS = {
    "site_title": "N+1 Query Lab Admin",
    "site_header": "N+1 Query Lab",
    "site_brand": "N+1 Query Lab",
    "welcome_sign": "Manage your Books and Authors",
    "copyright": "N+1 Query Lab",
    "show_sidebar": True,
    "navigation_expanded": True,
    "icons": {
        "core.Author": "fas fa-user-pen",
        "core.AuthorProfile": "fas fa-id-card",
        "core.Book": "fas fa-book-open",
        "auth": "fas fa-users",
    },
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "n1query.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "n1query.wsgi.application"
ASGI_APPLICATION = "n1query.asgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = []
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
