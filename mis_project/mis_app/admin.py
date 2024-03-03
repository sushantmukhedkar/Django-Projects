# mis_app/admin.py
from django.contrib import admin  # Ensure this import is present
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Department, Employee, Project

class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department

class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee

class ProjectResource(resources.ModelResource):
    class Meta:
        model = Project

@admin.register(Department)
class DepartmentAdmin(ImportExportModelAdmin):
    resource_class = DepartmentResource

@admin.register(Employee)
class EmployeeAdmin(ImportExportModelAdmin):
    resource_class = EmployeeResource

@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    resource_class = ProjectResource
