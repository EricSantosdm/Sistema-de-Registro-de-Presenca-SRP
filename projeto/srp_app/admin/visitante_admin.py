from django.contrib import admin
from novadata_utils.admin import NovadataModelAdmin
from unfold.admin import ModelAdminMixin

from ..models import Visitante


@admin.register(Visitante)
class VisitanteAdmin(ModelAdminMixin, NovadataModelAdmin):
    search_fields = [
        "id",
        "nome_completo",
    ]
