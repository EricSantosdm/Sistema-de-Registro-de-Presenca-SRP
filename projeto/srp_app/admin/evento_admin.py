from django.contrib import admin
from novadata_utils.admin import NovadataModelAdmin
from novadata_utils.redirect import reverse_lazy_plus

from ..models import Evento
from .participante_evento_inline import ParticipanteEventoInline


@admin.register(Evento)
class EventoAdmin(NovadataModelAdmin):
    inlines = [
        ParticipanteEventoInline,
    ]

    change_actions = [
        "gerar_qrcode_inscreverse",
        # "gerar_qrcode_marcar_presenca",
    ]

    def gerar_qrcode_inscreverse(self, request, obj):
        """Redireciona para a view de gerar QRCode."""
        return reverse_lazy_plus(
            "gerar_qrcode",
            url_params=[obj.pk],
            get_params={
                "acao": "inscreverse",
            },
        )
