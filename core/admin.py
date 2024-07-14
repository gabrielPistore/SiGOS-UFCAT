from django.contrib import admin

from .models import Category, Employee, Report, WorkOrder


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin): ...


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): ...


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin): ...


@admin.register(WorkOrder)
class WorkOrderAdmin(admin.ModelAdmin): ...
