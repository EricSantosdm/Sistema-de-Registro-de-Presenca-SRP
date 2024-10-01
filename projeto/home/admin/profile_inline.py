from django.contrib import admin
from unfold.admin import TabularInline

from ..models import Profile


class ProfileInline(TabularInline, admin.StackedInline):
    model = Profile

    extra = 0

    min_num = 1

    can_delete = False

    fk_name = "usuario"

    exclude = [
        "usuario_criacao",
        "usuario_atualizacao",
    ]
