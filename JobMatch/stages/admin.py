from django.contrib import admin

from utils.export_csv import ExportCsv
from .models import Stage


# Register your models here.
@admin.register(Stage)
class StageAdmin(admin.ModelAdmin, ExportCsv):
    list_display = ('name', 'applied', 'phone', 'onsite', 'offer', 'company')

    actions = ["export_as_csv"]
