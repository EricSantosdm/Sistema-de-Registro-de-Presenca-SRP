from django.urls import path

from . import views

urlpatterns = [
    path(
        "increverse/<int:id_evento>/",
        views.inscreverse,
        name="inscreverse",
    ),
    path(
        "sucesso_inscricao/<int:pk>/",
        views.SucessoInscricaoView.as_view(),
        name="sucesso_inscricao",
    ),
]
