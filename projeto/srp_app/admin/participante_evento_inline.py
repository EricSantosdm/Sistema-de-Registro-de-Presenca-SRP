from django.contrib import admin

from ..models import ParticipanteEvento


class ParticipanteEventoInline(admin.TabularInline):
    model = ParticipanteEvento

    extra = 0

    autocomplete_fields = [
        "usuario",
    ]

    exclude = [
        "usuario_criacao",
        "usuario_atualizacao",
    ]
