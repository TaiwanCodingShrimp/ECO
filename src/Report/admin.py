from django.contrib import admin

from .models import Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ["report_id", "user_id", "date"]


admin.site.register(Report, ReportAdmin)
