from django.contrib import admin

from utils.export_csv import ExportCsv
from .models import Resume


# Register your models here.
@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin, ExportCsv):
    list_display = ('name', 'top_skills', 'current_job', 'loc')
    # list_filter = ('company', 'company_logo', 'cb_name',
    #                 'cb_company_logo', 'cb_domain')
    actions = ["export_as_csv"]
