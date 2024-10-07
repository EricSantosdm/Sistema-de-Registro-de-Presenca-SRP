from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework import routers

main_router = routers.DefaultRouter()

urlpatterns = (
    [
        path(
            "admin/",
            admin.site.urls,
        ),
        path(
            "",
            include("home.urls"),
        ),
        path(
            "srp_app/",
            include("srp_app.urls"),
        ),
        # Regsitragion urls
        path(
            "",
            include("django.contrib.auth.urls"),
        ),
        # APIs
        path(
            "api/",
            include(main_router.urls),
        ),
        path(
            "api-auth/",
            include("rest_framework.urls"),
        ),
        path(
            "api/schema/",
            login_required(SpectacularAPIView.as_view()),
            name="schema",
        ),
        path(
            "api/docs-swagger/",
            login_required(SpectacularSwaggerView.as_view(url_name="schema")),
            name="swagger",
        ),
        path(
            "api/docs-redoc/",
            login_required(SpectacularRedocView.as_view(url_name="schema")),
            name="redoc",
        ),
        # Libs urls
        path(
            "advanced_filters/",
            include("advanced_filters.urls"),
        ),
        path(
            "__reload__/",
            include("django_browser_reload.urls"),
        ),
        path(
            "__debug__/",
            include("debug_toolbar.urls"),
        ),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)

admin.site.site_header = "SRP"
admin.site.index_title = "Tela inicial"
admin.site.site_title = "SRP"
admin.site.site_url = None
