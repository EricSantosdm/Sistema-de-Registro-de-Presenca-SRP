import os
from pathlib import Path

from decouple import config
from dj_database_url import parse as dburl
from django.templatetags.static import static

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "ec2-3-84-152-70.compute-1.amazonaws.com",
    "registrodepresenca.srp.ufersa.dev.br",
    "srp.ufersa.dev.br",
]

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.inlines",
    "unfold.contrib.import_export",
    "unfold.contrib.guardian",
    "unfold.contrib.simple_history",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Apps
    "front_assets",
    "home",
    "srp_app",
    # Libs
    "advanced_filters",
    "debug_toolbar",
    "django_admin_listfilter_dropdown",
    "django_browser_reload",
    "django_full_crud",
    "django_object_actions",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "import_export",
    "novadata_utils",
    "qr_code",
    "rangefilter",
    "rest_framework",
    "widget_tweaks",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DEV = config("DEV", default=False, cast=bool)
if DEV:
    MIDDLEWARE += [
        "django_browser_reload.middleware.BrowserReloadMiddleware",
        # "debug_toolbar.middleware.DebugToolbarMiddleware",
    ]

    DEBUG_TOOLBAR_PANELS = [
        "debug_toolbar.panels.sql.SQLPanel",
        "debug_toolbar.panels.timer.TimerPanel",
    ]

MIDDLEWARE += ["crum.CurrentRequestUserMiddleware"]

ROOT_URLCONF = "srp.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

PRODUCAO = config("PRODUCAO", default=False, cast=bool)

WSGI_APPLICATION = "srp.wsgi.application"

USE_AWS = config("USE_AWS", default=False, cast=bool)
if USE_AWS:
    AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = "django-srp"
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": "max-age=86400",
    }
    AWS_LOCATION = "static"
    AWS_DEFAULT_ACL = None

    STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
    STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

    # s3 public media settings
    PUBLIC_MEDIA_LOCATION = "media"
    MEDIA_URL = "https://%s/%s/" % (
        AWS_S3_CUSTOM_DOMAIN,
        PUBLIC_MEDIA_LOCATION,
    )
    DEFAULT_FILE_STORAGE = "srp.storage_backends.PublicMediaStorage"
elif PRODUCAO:
    STATIC_URL = "/static/"
    MEDIA_URL = "/media/"

    STATIC_ROOT = os.path.join("/var/www/html/static")
    MEDIA_ROOT = os.path.join("/var/www/html/media")
else:
    STATIC_URL = "/static/"
    MEDIA_URL = "/media/"

    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

if PRODUCAO:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "postgres",
            "USER": "postgres",
            "PASSWORD": "passwordsrp2024",
            "HOST": "database-srp.cezmcekhri9w.us-east-1.rds.amazonaws.com",
            "PORT": "5432",
        }
    }
else:
    default_dburl = "sqlite:///" + os.path.join(BASE_DIR, "db.sqlite3")
    DATABASES = {
        "default": config(
            "DATABASE_URL",
            default=default_dburl,
            cast=dburl,
        )
    }

REST_FRAMEWORK = {
    # "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated"),  # noqa E501
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend"
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",  # noqa E501
    "PAGE_SIZE": 10,
}

SPECTACULAR_SETTINGS = {
    "TITLE": "srp API",
    "DESCRIPTION": "srp description",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa E501
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa E501
    },
]

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = "admin:index"
LOGOUT_REDIRECT_URL = "admin:login"
LOGIN_URL = "admin:login"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = config("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", "")
DEFAULT_FROM_EMAIL = "srp <example@email.com.br>"

CLEAR_CACHE_ON_RESTART = True
UNFOLD = {
    "SITE_ICON": {
        "light": lambda request: static("srp_app/srp_logo.png"),
        "dark": lambda request: static("srp_app/srp_logo.png"),
    },
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("srp_app/srp_logo.png"),
        },
    ],
    "SCRIPTS": [
        lambda request: static("srp_app/changeLoginMessage.js"),
    ],
}
