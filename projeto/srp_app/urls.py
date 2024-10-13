from django.urls import path

from . import views

urlpatterns = [
    path(
        "qrcode/<int:pk>/",
        views.GerarQrCodeView.as_view(),
        name="gerar_qrcode",
    ),
    path(
        "inscreverse/<int:id_evento>/",
        views.inscreverse,
        name="inscreverse",
    ),
    path(
        "ja_inscrito/<int:pk>/",
        views.JaInscritoView.as_view(),
        name="ja_inscrito",
    ),
    path(
        "marcar_presenca/<int:id_evento>/",
        views.marcar_presenca,
        name="marcar_presenca",
    ),
    path(
        "sucesso_inscricao/<int:pk>/",
        views.SucessoInscricaoView.as_view(),
        name="sucesso_inscricao",
    ),
    path(
        "sucesso_presenca/<int:pk>/",
        views.SucessoPresencaView.as_view(),
        name="sucesso_presenca",
    ),
]
