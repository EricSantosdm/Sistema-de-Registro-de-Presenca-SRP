from django.contrib import admin
from unfold.admin import TabularInline

from ..models import ParticipanteEvento


class ParticipanteEventoInline(TabularInline, admin.TabularInline):
    model = ParticipanteEvento

    extra = 0

    autocomplete_fields = [
        "usuario",
    ]

    exclude = [
        "usuario_criacao",
        "usuario_atualizacao",
    ]
