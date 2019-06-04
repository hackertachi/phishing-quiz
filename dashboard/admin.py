from django.contrib import admin
from mainapp.models import UsersModel
from import_export.admin import ImportExportModelAdmin


@admin.register(UsersModel)
class UsersModelAdmin(ImportExportModelAdmin):
	pass