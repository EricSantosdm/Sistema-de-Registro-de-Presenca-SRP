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

urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        "",
        include("home.urls"),
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
