from django.urls import path

from . import views

urlpatterns = [
    path(
        "increverse/<int:id_evento>/",
        views.inscreverse,
        name="inscreverse",
    ),
]
