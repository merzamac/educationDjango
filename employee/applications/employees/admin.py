from django.contrib import admin
from .models import  *

# Register your models here.

admin.site.register(Skill)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'second_name',
        'department',
        'job',
        'full_name',
    )
    def full_name(self, obj):
        return obj.first_name + ' ' + obj.second_name

    search_fields = ('first_name',)
    list_filter = ('job','skills')
    filter_horizontal = ('skills',)
admin.site.register(Employee,EmployeeAdmin)