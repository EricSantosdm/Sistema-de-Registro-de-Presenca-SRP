from django.contrib import admin
from novadata_utils.admin import NovadataModelAdmin
from unfold.admin import ModelAdmin

from ..models import ParticipanteEvento


@admin.register(ParticipanteEvento)
class ParticipanteEventoAdmin(ModelAdmin, NovadataModelAdmin):
    extra = 0

    autocomplete_fields = [
        "usuario",
    ]

    exclude = [
        "usuario_criacao",
        "usuario_atualizacao",
    ]
