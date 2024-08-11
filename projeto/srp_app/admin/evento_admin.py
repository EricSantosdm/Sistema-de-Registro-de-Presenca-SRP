from django.contrib import admin
from novadata_utils.admin import NovadataModelAdmin

from ..models import Evento
from .participante_evento_inline import ParticipanteEventoInline


@admin.register(Evento)
class EventoAdmin(NovadataModelAdmin):
    inlines = [
        ParticipanteEventoInline,
    ]
