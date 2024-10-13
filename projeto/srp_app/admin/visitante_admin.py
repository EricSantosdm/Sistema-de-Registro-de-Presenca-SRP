from django.contrib import admin
from novadata_utils.admin import NovadataModelAdmin
from unfold.admin import ModelAdmin

from ..models import Visitante


@admin.register(Visitante)
class VisitanteAdmin(NovadataModelAdmin, ModelAdmin):
    search_fields = [
        "id",
        "nome_completo",
    ]
