from django.contrib import admin
from novadata_utils.admin import NovadataModelAdmin
from novadata_utils.redirect import reverse_lazy_plus
from unfold.admin import ModelAdminMixin
from unfold.contrib.filters.admin import RangeDateFilter, RangeDateTimeFilter

from ..models import Evento
from .participante_evento_inline import ParticipanteEventoInline


@admin.register(Evento)
class EventoAdmin(ModelAdminMixin, NovadataModelAdmin):
    inlines = [
        ParticipanteEventoInline,
    ]

    change_actions = [
        "gerar_qrcode_inscricao",
        "gerar_qrcode_presenca",
    ]

    def gerar_qrcode_inscricao(self, request, obj):
        """Redireciona para a view de gerar QRCode."""
        return reverse_lazy_plus(
            "gerar_qrcode",
            url_params=[obj.pk],
            get_params={
                "acao": "inscreverse",
            },
        )

    def gerar_qrcode_presenca(self, request, obj):
        """Redireciona para a view de gerar QRCode."""
        return reverse_lazy_plus(
            "gerar_qrcode",
            url_params=[obj.pk],
            get_params={
                "acao": "marcar_presenca",
            },
        )
