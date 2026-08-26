from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import (
    Asset,
    Employee,
    AssetTransfer,
    MaintenanceRecord,
)


@login_required
def dashboard(request):
    context = {
        "total_assets": Asset.objects.count(),

        "available_assets": Asset.objects.filter(
            status="available"
        ).count(),

        "assigned_assets": Asset.objects.filter(
            status="assigned"
        ).count(),

        "maintenance_assets": Asset.objects.filter(
            status="maintenance"
        ).count(),

        "retired_assets": Asset.objects.filter(
            status="retired"
        ).count(),

        "total_employees": Employee.objects.count(),

        "recent_transfers": AssetTransfer.objects.select_related(
            "asset",
            "from_employee",
            "to_employee",
            "from_location",
            "to_location",
        ).order_by("-transferred_at")[:5],

        "recent_maintenance": MaintenanceRecord.objects.select_related(
            "asset"
        ).order_by("-reported_at")[:5],
    }

    return render(
        request,
        "assets/dashboard.html",
        context,
    )


@login_required
def assets_list(request):
    assets = Asset.objects.all().order_by("asset_tag")

    return render(
        request,
        "assets/assets_list.html",
        {
            "assets": assets,
        },
    )