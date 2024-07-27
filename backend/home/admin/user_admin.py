from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin

from .profile_inline import ProfileInline

admin.site.unregister(User)


@admin.register(User)
class CustomUserAdmin(ImportExportModelAdmin, UserAdmin):
    inlines = [ProfileInline]
