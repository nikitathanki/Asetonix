from django.contrib import admin
from .models import Asset, Employee, AssetAssignment, AssetHistory


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = (
        "asset_tag",
        "name",
        "category",
        "status",
        "condition",
        "location",
    )

    list_filter = (
        "status",
        "condition",
        "category",
    )

    search_fields = (
        "asset_tag",
        "name",
        "serial_number",
        "brand",
        "model",
    )


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        "employee_id",
        "name",
        "email",
        "department",
        "designation",
        "status",
    )

    list_filter = (
        "department",
        "status",
    )

    search_fields = (
        "employee_id",
        "name",
        "email",
        "department",
    )


@admin.register(AssetAssignment)
class AssetAssignmentAdmin(admin.ModelAdmin):
    list_display = (
        "asset",
        "employee",
        "assigned_at",
        "returned_at",
        "is_active",
    )

    list_filter = (
        "assigned_at",
        "returned_at",
    )

    search_fields = (
        "asset__asset_tag",
        "asset__name",
        "employee__employee_id",
        "employee__name",
    )


@admin.register(AssetHistory)
class AssetHistoryAdmin(admin.ModelAdmin):
    list_display = (
        "asset",
        "event_type",
        "performed_by",
        "created_at",
    )

    list_filter = (
        "event_type",
        "created_at",
    )

    search_fields = (
        "asset__asset_tag",
        "asset__name",
        "description",
        "performed_by",
    )

    readonly_fields = (
        "created_at",
    )