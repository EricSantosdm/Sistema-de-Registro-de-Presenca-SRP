from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django_weasyprint import WeasyTemplateResponseMixin
from novadata_utils.redirect import reverse_lazy_plus
from srp_app.models import Evento


class GerarQrCodeView(
    LoginRequiredMixin,
    WeasyTemplateResponseMixin,
    DetailView,
):
    model = Evento

    template_name = "srp_app/qr_code.html"

    def get_path(self):
        """Retorna o path do QRCode."""
        acao = self.request.GET.get("acao")
        evento = self.get_object()

        if acao == "inscreverse":
            path = reverse_lazy_plus(
                "inscreverse",
                url_params=[evento.pk],
                just_uri=True,
            )
        elif acao == "marcar_presenca":
            path = reverse_lazy_plus(
                "marcar_presenca",
                url_params=[evento.pk],
                just_uri=True,
            )
        else:
            raise ValueError("Ação inválida.")

        return path

    def get_title_and_text(self):
        """Retorna o título e o texto do QRCode."""
        acao = self.request.GET.get("acao")
        evento = self.get_object()

        if acao == "inscreverse":
            title = f"Inscrição no evento {evento}"
            text = f"Ao escanear este QR code, você se inscreverá no evento {evento}."  # noqa E501
        elif acao == "marcar_presenca":
            title = f"Presença no evento {evento}"
            text = f"Ao escanear este QR code, você marcará sua presença no evento {evento}."  # noqa E501
        else:
            raise ValueError("Ação inválida.")

        return title, text

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        """Retorna o contexto da view."""
        context = super().get_context_data(**kwargs)

        host = self.request._current_scheme_host
        path = self.get_path()
        rota = f"{host}{path}"

        context["rota"] = rota

        title, text = self.get_title_and_text()
        context["title"] = title
        context["text"] = text

        return context
