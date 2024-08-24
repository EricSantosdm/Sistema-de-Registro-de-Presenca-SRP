from django.contrib import admin
from novadata_utils.admin import NovadataModelAdmin

from ..models import Visitante


@admin.register(Visitante)
class VisitanteAdmin(NovadataModelAdmin):
    search_fields = [
        "id",
        "nome_completo",
    ]
