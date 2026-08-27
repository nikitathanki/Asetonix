from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import (
    Asset,
    Employee,
    AssetTransfer,
    AssetAssignment,
    MaintenanceRecord,
)


# =========================================================
# DASHBOARD
# =========================================================

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


# =========================================================
# ASSETS LIST
# =========================================================

@login_required
def assets_list(request):

    assets = Asset.objects.all().order_by("asset_tag")

    context = {
        "assets": assets,

        "available_count": Asset.objects.filter(
            status="available"
        ).count(),

        "assigned_count": Asset.objects.filter(
            status="assigned"
        ).count(),

        "maintenance_count": Asset.objects.filter(
            status="maintenance"
        ).count(),
    }

    return render(
        request,
        "assets/assets_list.html",
        context,
    )


# =========================================================
# ASSET DETAIL
# =========================================================

@login_required
def asset_detail(request, asset_tag):

    asset = get_object_or_404(
        Asset,
        asset_tag=asset_tag,
    )

    active_assignment = AssetAssignment.objects.filter(
        asset=asset,
        returned_at__isnull=True,
    ).select_related(
        "employee",
    ).first()

    maintenance_records = MaintenanceRecord.objects.filter(
        asset=asset
    ).order_by("-reported_at")

    return render(
        request,
        "assets/asset_detail.html",
        {
            "asset": asset,
            "active_assignment": active_assignment,
            "maintenance_records": maintenance_records,
        },
    )

# =========================================================
# ASSIGN ASSET
# =========================================================

@login_required
def assign_asset(request, asset_tag):

    asset = get_object_or_404(
        Asset,
        asset_tag=asset_tag,
    )

    active_assignment = AssetAssignment.objects.filter(
        asset=asset,
        returned_at__isnull=True,
    ).select_related(
        "employee",
    ).first()

    employees = Employee.objects.filter(
        status="active"
    ).order_by("name")

    # -------------------------
    # FORM SUBMISSION
    # -------------------------

    if request.method == "POST":

        if active_assignment:

            messages.error(
                request,
                "This asset is already assigned.",
            )

            return redirect(
                "asset_detail",
                asset_tag=asset.asset_tag,
            )

        employee_id = request.POST.get("employee")

        notes = request.POST.get(
            "notes",
            "",
        ).strip()

        if not employee_id:

            messages.error(
                request,
                "Please select an employee.",
            )

            return render(
                request,
                "assets/assign_asset.html",
                {
                    "asset": asset,
                    "employees": employees,
                    "active_assignment": active_assignment,
                },
            )

        employee = get_object_or_404(
            Employee,
            pk=employee_id,
            status="active",
        )

        AssetAssignment.objects.create(
            asset=asset,
            employee=employee,
            notes=notes,
        )

        messages.success(
            request,
            f"{asset.asset_tag} has been assigned to "
            f"{employee.name}.",
        )

        return redirect(
            "asset_detail",
            asset_tag=asset.asset_tag,
        )

    # -------------------------
    # OPEN ASSIGN PAGE
    # -------------------------

    return render(
        request,
        "assets/assign_asset.html",
        {
            "asset": asset,
            "employees": employees,
            "active_assignment": active_assignment,
        },
    )


# =========================================================
# TRANSFER ASSET
# =========================================================

@login_required
def transfer_asset(request, asset_tag):

    asset = get_object_or_404(
        Asset,
        asset_tag=asset_tag,
    )

    active_assignment = AssetAssignment.objects.filter(
        asset=asset,
        returned_at__isnull=True,
    ).select_related(
        "employee",
    ).first()

    employees = Employee.objects.filter(
        status="active"
    ).order_by("name")

    # -------------------------
    # FORM SUBMISSION
    # -------------------------

    if request.method == "POST":

        employee_id = request.POST.get("employee")

        reason = request.POST.get(
            "reason",
            "",
        ).strip()

        notes = request.POST.get(
            "notes",
            "",
        ).strip()

        if not employee_id:

            messages.error(
                request,
                "Please select an employee.",
            )

            return render(
                request,
                "assets/transfer_asset.html",
                {
                    "asset": asset,
                    "active_assignment": active_assignment,
                    "employees": employees,
                },
            )

        to_employee = get_object_or_404(
            Employee,
            pk=employee_id,
            status="active",
        )

        from_employee = (
            active_assignment.employee
            if active_assignment
            else None
        )

        if (
            from_employee
            and from_employee.pk == to_employee.pk
        ):

            messages.error(
                request,
                "The asset is already assigned to this employee.",
            )

            return render(
                request,
                "assets/transfer_asset.html",
                {
                    "asset": asset,
                    "active_assignment": active_assignment,
                    "employees": employees,
                },
            )

        # -------------------------
        # CREATE TRANSFER RECORD
        # -------------------------

        transfer = AssetTransfer.objects.create(
            asset=asset,
            from_employee=from_employee,
            to_employee=to_employee,
            from_location=asset.location,
            to_location=asset.location,
            reason=reason,
            notes=notes,
        )

        # -------------------------
        # CLOSE OLD ASSIGNMENT
        # -------------------------

        if active_assignment:

            active_assignment.returned_at = (
                transfer.transferred_at
            )

            active_assignment.save()

        # -------------------------
        # CREATE NEW ASSIGNMENT
        # -------------------------

        AssetAssignment.objects.create(
            asset=asset,
            employee=to_employee,
            notes=f"Transferred asset. {notes}".strip(),
        )

        messages.success(
            request,
            f"{asset.asset_tag} has been transferred to "
            f"{to_employee.name}.",
        )

        return redirect(
            "asset_detail",
            asset_tag=asset.asset_tag,
        )

    # -------------------------
    # OPEN TRANSFER PAGE
    # -------------------------

    return render(
        request,
        "assets/transfer_asset.html",
        {
            "asset": asset,
            "active_assignment": active_assignment,
            "employees": employees,
        },
    )

    # =========================================================
# REPORT MAINTENANCE
# =========================================================

@login_required
def report_maintenance(request, asset_tag):

    asset = get_object_or_404(
        Asset,
        asset_tag=asset_tag,
    )

    if request.method == "POST":

        title = request.POST.get(
            "title",
            "",
        ).strip()

        description = request.POST.get(
            "description",
            "",
        ).strip()

        priority = request.POST.get(
            "priority",
            "medium",
        )

        technician = request.POST.get(
            "technician",
            "",
        ).strip()

        cost = request.POST.get(
            "cost",
            "",
        ).strip()

        notes = request.POST.get(
            "notes",
            "",
        ).strip()

        if not title:

            messages.error(
                request,
                "Please enter a maintenance title.",
            )

            return render(
                request,
                "assets/report_maintenance.html",
                {
                    "asset": asset,
                },
            )

        MaintenanceRecord.objects.create(
            asset=asset,
            title=title,
            description=description,
            priority=priority,
            technician=technician,
            cost=cost if cost else None,
            notes=notes,
        )

        messages.success(
            request,
            f"Maintenance has been reported for "
            f"{asset.asset_tag}.",
        )

        return redirect(
            "asset_detail",
            asset_tag=asset.asset_tag,
        )

    return render(
        request,
        "assets/report_maintenance.html",
        {
            "asset": asset,
        },
    )

# =========================================================
# MAINTENANCE LIST
# =========================================================

@login_required
def maintenance_list(request):

    maintenance_records = MaintenanceRecord.objects.select_related(
        "asset"
    ).order_by("-reported_at")

    context = {
        "maintenance_records": maintenance_records,

        "total_count": MaintenanceRecord.objects.count(),

        "reported_count": MaintenanceRecord.objects.filter(
            status="reported"
        ).count(),

        "in_progress_count": MaintenanceRecord.objects.filter(
            status="in_progress"
        ).count(),

        "completed_count": MaintenanceRecord.objects.filter(
            status="completed"
        ).count(),

        "cancelled_count": MaintenanceRecord.objects.filter(
            status="cancelled"
        ).count(),
    }

    return render(
        request,
        "assets/maintenance_list.html",
        context,
    )