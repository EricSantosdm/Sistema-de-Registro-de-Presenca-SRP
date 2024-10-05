from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin
from unfold.admin import ModelAdminMixin

admin.site.unregister(Group)


@admin.register(Group)
class GroupAdmin(ModelAdminMixin, BaseGroupAdmin, ImportExportModelAdmin):
    pass
