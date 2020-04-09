from django.contrib import admin

from .models import Company, Task

class CompanyModelAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'address', 'created', 'updated'
    ]

    class Meta:
        model = Company

admin.site.register(Company, CompanyModelAdmin)

class TaskModelAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'duration', 'dependencies', 'resources'
    ]

    class Meta:
        model = Task

admin.site.register(Task, TaskModelAdmin)