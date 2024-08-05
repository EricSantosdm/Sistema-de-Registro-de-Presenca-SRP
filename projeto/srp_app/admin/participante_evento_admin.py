from django.contrib import admin
from novadata_utils.admin import NovadataModelAdmin

from ..models import ParticipanteEvento


@admin.register(ParticipanteEvento)
class ParticipanteEventoAdmin(NovadataModelAdmin):
    pass
