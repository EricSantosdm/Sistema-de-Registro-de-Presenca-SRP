from django.contrib import admin
from django.urls import path
from django.utils.html import format_html
from django.views.generic import DetailView
from novadata_utils.admin import NovadataModelAdmin
from novadata_utils.redirect import reverse_lazy_plus
from unfold.admin import ModelAdmin
from unfold.decorators import action
from unfold.views import UnfoldModelAdminViewMixin

from ..models import Evento
from .participante_evento_inline import ParticipanteEventoInline


class InscreverseEventoView(UnfoldModelAdminViewMixin, DetailView):
    title = "Increver-se no evento"

    permission_required = ()

    template_name = "home/evento/inscreverse.html"

    model = Evento


@admin.register(Evento)
class EventoAdmin(NovadataModelAdmin, ModelAdmin):
    inlines = [
        ParticipanteEventoInline,
    ]

    change_actions = [
        "gerar_qrcode_inscricao",
        "gerar_qrcode_presenca",
    ]

    def get_list_display(self, request):
        return super().get_list_display(request) + ["participantes"]

    @action(attrs={"target": "_blank"})
    def gerar_qrcode_inscricao(self, request, obj):
        """Redireciona para a view de gerar QRCode."""
        return reverse_lazy_plus(
            "gerar_qrcode",
            url_params=[obj.pk],
            get_params={
                "acao": "inscreverse",
            },
        )

    @action(attrs={"target": "_blank"})
    def gerar_qrcode_presenca(self, request, obj):
        """Redireciona para a view de gerar QRCode."""
        return reverse_lazy_plus(
            "gerar_qrcode",
            url_params=[obj.pk],
            get_params={
                "acao": "marcar_presenca",
            },
        )

    def get_urls(self):
        return [
            path(
                "<int:pk>/inscreverse/",
                self.admin_site.admin_view(
                    InscreverseEventoView.as_view(
                        model_admin=self,
                    )
                ),
                name="srp_app_evento_inscreverse",
            ),
            *super().get_urls(),
        ]

    def participantes(self, obj: Evento) -> str:
        """Redireciona para os participantes desse evento."""
        link = reverse_lazy_plus(
            "admin:srp_app_participanteevento_changelist",
            get_params={
                "evento__id__exact": obj.pk,
            },
            just_uri=True,
        )

        return format_html(
            f'<a href="{link}" target="_blank">Participantes</a>'
        )
