from django.contrib import admin

from api.models import Firm, Employee


class FirmAdmin(admin.ModelAdmin):
    list_display = ['name']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'firm']



admin.site.register(Firm, FirmAdmin)
admin.site.register(Employee, EmployeeAdmin)
