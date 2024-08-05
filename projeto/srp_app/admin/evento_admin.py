from django.contrib import admin
from novadata_utils.admin import NovadataModelAdmin

from ..models import Evento


@admin.register(Evento)
class EventoAdmin(NovadataModelAdmin):
    pass
