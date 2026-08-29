from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.db.models import Count, Q
from django.contrib.auth.models import User, Group
import csv

from django.http import HttpResponse


from .models import (
    Asset,
    Employee,
    AssetTransfer,
    AssetAssignment,
    MaintenanceRecord,
    AssetHistory,
    Department,
    Location,
    Category,

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

        "retired_count": Asset.objects.filter(
            status="retired"
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

    asset_history = asset.history.all()

    return render(
        request,
        "assets/asset_detail.html",
        {
            "asset": asset,
            "active_assignment": active_assignment,
            "maintenance_records": maintenance_records,
            "asset_history": asset_history,
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

    if asset.status == "retired":

        messages.error(
            request,
            "A retired asset cannot be assigned.",
        )

        return redirect(
            "asset_detail",
            asset_tag=asset.asset_tag,
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

    if asset.status == "retired":

        messages.error(
            request,
            "A retired asset cannot be transferred.",
        )

        return redirect(
            "asset_detail",
            asset_tag=asset.asset_tag,
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

        transfer = AssetTransfer.objects.create(
            asset=asset,
            from_employee=from_employee,
            to_employee=to_employee,
            from_location=asset.location,
            to_location=asset.location,
            reason=reason,
            notes=notes,
        )

        if active_assignment:

            active_assignment.returned_at = (
                transfer.transferred_at
            )

            active_assignment.save()

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

    if asset.status == "retired":

        messages.error(
            request,
            "Maintenance cannot be reported for a retired asset.",
        )

        return redirect(
            "asset_detail",
            asset_tag=asset.asset_tag,
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


# =========================================================
# ASSIGNMENTS LIST
# =========================================================

@login_required
def assignments_list(request):

    assignments = (
        AssetAssignment.objects
        .select_related(
            "asset",
            "employee",
        )
        .order_by("-assigned_at")
    )

    total_assignments = assignments.count()

    active_assignments = assignments.filter(
        returned_at__isnull=True
    ).count()

    returned_assignments = assignments.filter(
        returned_at__isnull=False
    ).count()

    context = {
        "assignments": assignments,
        "total_assignments": total_assignments,
        "active_assignments": active_assignments,
        "returned_assignments": returned_assignments,
    }

    return render(
        request,
        "assets/assignments_list.html",
        context,
    )


# =========================================================
# TRANSFERS LIST
# =========================================================

@login_required
def transfers_list(request):

    transfers = AssetTransfer.objects.select_related(
        "asset",
        "from_employee",
        "to_employee",
        "from_location",
        "to_location",
    ).order_by("-transferred_at")

    context = {
        "transfers": transfers,

        "total_transfers": AssetTransfer.objects.count(),

        "today_transfers": AssetTransfer.objects.filter(
            transferred_at__date=timezone.localdate()
        ).count(),
    }

    return render(
        request,
        "assets/transfers_list.html",
        context,
    )


# =========================================================
# RETIREMENTS LIST
# =========================================================

@login_required
def retirements_list(request):

    retired_assets = Asset.objects.filter(
        status="retired"
    ).select_related(
        "category",
        "location",
    ).order_by("asset_tag")

    context = {
        "retired_assets": retired_assets,
        "total_retired": retired_assets.count(),
    }

    return render(
        request,
        "assets/retirements_list.html",
        context,
    )


# =========================================================
# RETIRE ASSET
# =========================================================

@login_required
def retire_asset(request, asset_tag):

    asset = get_object_or_404(
        Asset,
        asset_tag=asset_tag,
    )

    # -----------------------------------------------------
    # ALREADY RETIRED
    # -----------------------------------------------------

    if asset.status == "retired":

        messages.info(
            request,
            f"{asset.asset_tag} is already retired.",
        )

        return redirect(
            "asset_detail",
            asset_tag=asset.asset_tag,
        )

    # -----------------------------------------------------
    # FORM SUBMISSION
    # -----------------------------------------------------

    if request.method == "POST":

        reason = request.POST.get(
            "reason",
            "",
        ).strip()

        notes = request.POST.get(
            "notes",
            "",
        ).strip()

        if not reason:

            messages.error(
                request,
                "Please select a retirement reason.",
            )

            return render(
                request,
                "assets/retire_asset.html",
                {
                    "asset": asset,
                    "reason": reason,
                    "notes": notes,
                },
            )

        with transaction.atomic():

            # -------------------------------------------------
            # CLOSE ACTIVE ASSIGNMENT
            # -------------------------------------------------

            active_assignment = (
                AssetAssignment.objects
                .filter(
                    asset=asset,
                    returned_at__isnull=True,
                )
                .first()
            )

            if active_assignment:

                active_assignment.returned_at = timezone.now()
                active_assignment.save()

            # -------------------------------------------------
            # RETIRE ASSET
            # -------------------------------------------------

            asset.status = "retired"

            asset.save(
                update_fields=[
                    "status",
                    "updated_at",
                ]
            )

            # -------------------------------------------------
            # CREATE RETIREMENT HISTORY
            # -------------------------------------------------

            history_description = (
                f"Asset retired. "
                f"Reason: {reason}."
            )

            if notes:

                history_description += (
                    f" Notes: {notes}"
                )

            AssetHistory.objects.create(
                asset=asset,
                event_type="retired",
                description=history_description,
                performed_by=request.user.get_username(),
            )

        messages.success(
            request,
            f"{asset.asset_tag} has been retired successfully.",
        )

        return redirect(
            "retirements_list",
        )

    # -----------------------------------------------------
    # OPEN RETIREMENT PAGE
    # -----------------------------------------------------

    return render(
        request,
        "assets/retire_asset.html",
        {
            "asset": asset,
        },
    )


# =========================================================
# ASSET HEALTH
# =========================================================

@login_required
def asset_health(request):

    assets = Asset.objects.all().order_by("asset_tag")

    asset_health_data = []

    for asset in assets:

        score = 100

        # -------------------------------------------------
        # CONDITION IMPACT
        # -------------------------------------------------

        condition = str(asset.condition).lower()

        if condition == "good":
            score -= 10

        elif condition == "fair":
            score -= 25

        elif condition == "poor":
            score -= 45

        elif condition == "damaged":
            score -= 60

        # -------------------------------------------------
        # STATUS IMPACT
        # -------------------------------------------------

        status = str(asset.status).lower()

        if status == "maintenance":
            score -= 25

        elif status == "retired":
            score = 0

        # -------------------------------------------------
        # MAINTENANCE HISTORY IMPACT
        # -------------------------------------------------

        maintenance_count = MaintenanceRecord.objects.filter(
            asset=asset
        ).count()

        score -= min(maintenance_count * 5, 20)

        # -------------------------------------------------
        # KEEP SCORE IN RANGE
        # -------------------------------------------------

        score = max(0, min(score, 100))

        # -------------------------------------------------
        # HEALTH LEVEL
        # -------------------------------------------------

        if score >= 80:
            health_level = "Excellent"

        elif score >= 60:
            health_level = "Good"

        elif score >= 40:
            health_level = "Fair"

        else:
            health_level = "Poor"

        asset_health_data.append(
            {
                "asset": asset,
                "score": score,
                "health_level": health_level,
                "maintenance_count": maintenance_count,
            }
        )

    return render(
        request,
        "assets/asset_health.html",
        {
            "asset_health_data": asset_health_data,
        },
    )


# =========================================================
# UTILIZATION
# =========================================================

@login_required
def utilization(request):

    assets = Asset.objects.all().order_by("asset_tag")

    total_assets = assets.count()

    assigned_assets = assets.filter(
        status="assigned"
    ).count()

    available_assets = assets.filter(
        status="available"
    ).count()

    maintenance_assets = assets.filter(
        status="maintenance"
    ).count()

    retired_assets = assets.filter(
        status="retired"
    ).count()

    utilization_rate = 0

    if total_assets > 0:

        utilization_rate = round(
            (assigned_assets / total_assets) * 100,
            1,
        )

    return render(
        request,
        "assets/utilization.html",
        {
            "total_assets": total_assets,
            "assigned_assets": assigned_assets,
            "available_assets": available_assets,
            "maintenance_assets": maintenance_assets,
            "retired_assets": retired_assets,
            "utilization_rate": utilization_rate,
        },
    )


# =========================================================
# RISK ANALYSIS
# =========================================================

@login_required
def risk_analysis(request):

    assets = Asset.objects.all().order_by("asset_tag")

    total_assets = assets.count()

    low_risk_count = 0
    medium_risk_count = 0
    high_risk_count = 0

    risk_assets = []

    for asset in assets:

        # -------------------------------------------------
        # MAINTENANCE HISTORY
        # -------------------------------------------------

        maintenance_count = (
            MaintenanceRecord.objects
            .filter(asset=asset)
            .count()
        )

        # -------------------------------------------------
        # RISK SCORE
        # -------------------------------------------------

        risk_score = 0

        # Asset condition

        condition = str(
            getattr(asset, "condition", "")
        ).lower()

        if condition in ["poor", "damaged"]:
            risk_score += 40

        elif condition in ["fair", "used"]:
            risk_score += 20

        elif condition == "new":
            risk_score += 5

        # Asset status

        status = str(
            getattr(asset, "status", "")
        ).lower()

        if status == "maintenance":
            risk_score += 30

        elif status == "assigned":
            risk_score += 10

        elif status == "available":
            risk_score += 5

        elif status == "retired":
            risk_score += 0

        # Maintenance history

        if maintenance_count >= 5:
            risk_score += 30

        elif maintenance_count >= 3:
            risk_score += 20

        elif maintenance_count >= 1:
            risk_score += 10

        # Maximum score = 100

        risk_score = min(risk_score, 100)

        # -------------------------------------------------
        # RISK LEVEL
        # -------------------------------------------------

        if risk_score >= 60:

            risk_level = "High"
            high_risk_count += 1

        elif risk_score >= 30:

            risk_level = "Medium"
            medium_risk_count += 1

        else:

            risk_level = "Low"
            low_risk_count += 1

        risk_assets.append(
            {
                "asset": asset,
                "risk_score": risk_score,
                "risk_level": risk_level,
                "maintenance_count": maintenance_count,
            }
        )

    # -----------------------------------------------------
    # CONTEXT
    # -----------------------------------------------------

    context = {
        "total_assets": total_assets,
        "low_risk_count": low_risk_count,
        "medium_risk_count": medium_risk_count,
        "high_risk_count": high_risk_count,
        "risk_assets": risk_assets,
    }

    return render(
        request,
        "assets/risk_analysis.html",
        context,
    )


# =========================================================
# COST ANALYSIS
# =========================================================

@login_required
def cost_analysis(request):

    assets = Asset.objects.all().order_by("asset_tag")

    total_assets = assets.count()

    total_maintenance_cost = 0

    asset_costs = []

    for asset in assets:

        maintenance_records = MaintenanceRecord.objects.filter(
            asset=asset
        )

        asset_cost = 0

        for record in maintenance_records:

            cost = getattr(record, "cost", 0) or 0

            asset_cost += cost

        total_maintenance_cost += asset_cost

        asset_costs.append(
            {
                "asset": asset,
                "maintenance_count": maintenance_records.count(),
                "maintenance_cost": asset_cost,
            }
        )

    context = {
        "total_assets": total_assets,
        "total_maintenance_cost": total_maintenance_cost,
        "asset_costs": asset_costs,
    }

    return render(
        request,
        "assets/cost_analysis.html",
        context,
    )


# =========================================================
# AUDIT TRAIL
# =========================================================

@login_required
def audit_trail(request):

    audit_records = (
        AssetHistory.objects
        .select_related("asset")
        .order_by("-created_at")
    )

    context = {
        "audit_records": audit_records,
        "total_records": audit_records.count(),
    }

    return render(
        request,
        "assets/audit_trail.html",
        context,
    )


# =========================================================
# CATEGORIES
# =========================================================

@login_required
def categories(request):

    categories = (
        Category.objects
        .annotate(
            asset_count=Count("assets")
        )
        .order_by("name")
    )

    context = {
        "categories": categories,
        "total_categories": categories.count(),
        "active_categories": categories.filter(
            is_active=True
        ).count(),
    }

    return render(
        request,
        "assets/categories.html",
        context,
    )


# =========================================================
# BRANDS
# =========================================================

@login_required
def brands(request):

    brands = (
        Asset.objects
        .exclude(brand="")
        .exclude(brand__isnull=True)
        .values("brand")
        .annotate(
            asset_count=Count("id")
        )
        .order_by("brand")
    )

    total_brands = brands.count()

    active_brands = total_brands

    context = {
        "brands": brands,
        "total_brands": total_brands,
        "active_brands": active_brands,
    }

    return render(
        request,
        "assets/brands.html",
        context,
    )


# =========================================================
# MODELS
# =========================================================

@login_required
def models_list(request):

    asset_models = (
        Asset.objects
        .exclude(model="")
        .exclude(model__isnull=True)
        .values("model")
        .annotate(
            asset_count=Count("id"),
            active_asset_count=Count(
                "id",
                filter=~Q(status="retired"),
            ),
        )
        .order_by("model")
    )

    total_models = asset_models.count()

    active_models = sum(
        1
        for item in asset_models
        if item["active_asset_count"] > 0
    )

    context = {
        "asset_models": asset_models,
        "total_models": total_models,
        "active_models": active_models,
    }

    return render(
        request,
        "assets/models.html",
        context,
    )


# =========================================================
# DEPARTMENTS
# =========================================================

@login_required
def departments(request):

    departments = (
        Department.objects
        .annotate(
            employee_count=Count("employees"),
            active_employee_count=Count(
                "employees",
                filter=Q(employees__status="active"),
            ),
        )
        .order_by("name")
    )

    total_departments = departments.count()

    active_departments = Department.objects.filter(
        is_active=True
    ).count()

    context = {
        "departments": departments,
        "total_departments": total_departments,
        "active_departments": active_departments,
    }

    return render(
        request,
        "assets/departments.html",
        context,
    )


# =========================================================
# LOCATIONS
# =========================================================

@login_required
def locations(request):

    locations = (
        Location.objects
        .annotate(
            asset_count=Count("assets"),
            active_asset_count=Count(
                "assets",
                filter=~Q(assets__status="retired"),
            ),
        )
        .order_by("name")
    )

    total_locations = locations.count()

    active_locations = Location.objects.filter(
        is_active=True
    ).count()

    context = {
        "locations": locations,
        "total_locations": total_locations,
        "active_locations": active_locations,
    }

    return render(
        request,
        "assets/locations.html",
        context,
    )


# =========================================================
# ALERTS
# =========================================================

@login_required
def alerts(request):

    # -----------------------------------------------------
    # HIGH RISK ASSETS
    # -----------------------------------------------------

    high_risk_assets = []

    assets = Asset.objects.all().order_by("asset_tag")

    for asset in assets:

        score = 100

        condition = str(asset.condition).lower()

        if condition == "good":
            score -= 10

        elif condition == "fair":
            score -= 25

        elif condition == "poor":
            score -= 45

        elif condition == "damaged":
            score -= 60

        status = str(asset.status).lower()

        if status == "maintenance":
            score -= 25

        elif status == "retired":
            score = 0

        maintenance_count = MaintenanceRecord.objects.filter(
            asset=asset
        ).count()

        score -= min(maintenance_count * 5, 20)

        score = max(0, min(score, 100))

        if status != "retired" and score < 40:

            high_risk_assets.append(
                {
                    "asset": asset,
                    "score": score,
                }
            )

    # -----------------------------------------------------
    # MAINTENANCE ALERTS
    # -----------------------------------------------------

    maintenance_assets = Asset.objects.filter(
        status="maintenance"
    ).order_by("asset_tag")

    # -----------------------------------------------------
    # RETURN ALERTS
    # -----------------------------------------------------

    active_assignments = (
        AssetAssignment.objects
        .filter(
            returned_at__isnull=True
        )
        .select_related(
            "asset",
            "employee",
        )
        .order_by("-assigned_at")
    )

    # -----------------------------------------------------
    # RETIRED ASSETS
    # -----------------------------------------------------

    retired_assets = Asset.objects.filter(
        status="retired"
    ).order_by("asset_tag")

    # -----------------------------------------------------
    # SUMMARY
    # -----------------------------------------------------

    context = {
        "high_risk_assets": high_risk_assets,
        "maintenance_assets": maintenance_assets,
        "active_assignments": active_assignments,
        "retired_assets": retired_assets,

        "high_risk_count": len(high_risk_assets),
        "maintenance_count": maintenance_assets.count(),
        "return_count": active_assignments.count(),
        "retired_count": retired_assets.count(),
    }

    return render(
        request,
        "assets/alerts.html",
        context,
    )


# =========================================================
# USERS & ROLES
# =========================================================

@login_required
def users_roles(request):

    users = User.objects.all().order_by("username")

    total_users = users.count()

    active_users = users.filter(
        is_active=True
    ).count()

    staff_users = users.filter(
        is_staff=True
    ).count()

    superusers = users.filter(
        is_superuser=True
    ).count()

    groups = Group.objects.all().order_by("name")

    context = {
        "users": users,
        "groups": groups,

        "total_users": total_users,
        "active_users": active_users,
        "staff_users": staff_users,
        "superusers": superusers,
    }

    return render(
        request,
        "assets/users_roles.html",
        context,
    )


# =========================================================
# REPORTS
# =========================================================

@login_required
def reports(request):

    # -----------------------------------------------------
    # ASSET SUMMARY
    # -----------------------------------------------------

    total_assets = Asset.objects.count()

    available_assets = Asset.objects.filter(
        status="available"
    ).count()

    assigned_assets = Asset.objects.filter(
        status="assigned"
    ).count()

    maintenance_assets = Asset.objects.filter(
        status="maintenance"
    ).count()

    retired_assets = Asset.objects.filter(
        status="retired"
    ).count()

    # -----------------------------------------------------
    # ORGANIZATION SUMMARY
    # -----------------------------------------------------

    total_employees = Employee.objects.count()

    total_categories = Category.objects.count()

    total_departments = Department.objects.count()

    total_locations = Location.objects.count()

    # -----------------------------------------------------
    # BRAND SUMMARY
    # -----------------------------------------------------

    total_brands = (
        Asset.objects
        .exclude(brand="")
        .exclude(brand__isnull=True)
        .values("brand")
        .distinct()
        .count()
    )

    # -----------------------------------------------------
    # MODEL SUMMARY
    # -----------------------------------------------------

    total_models = (
        Asset.objects
        .exclude(model="")
        .exclude(model__isnull=True)
        .values("model")
        .distinct()
        .count()
    )

    # -----------------------------------------------------
    # REPORT DATA
    # -----------------------------------------------------

    context = {
        "total_assets": total_assets,
        "available_assets": available_assets,
        "assigned_assets": assigned_assets,
        "maintenance_assets": maintenance_assets,
        "retired_assets": retired_assets,

        "total_employees": total_employees,
        "total_categories": total_categories,
        "total_brands": total_brands,
        "total_models": total_models,
        "total_departments": total_departments,
        "total_locations": total_locations,
    }

    return render(
        request,
        "assets/reports.html",
        context,
    )


@login_required
def export_data(request):

    export_type = request.GET.get("type")

    # =====================================================
    # ASSET DATA EXPORT
    # =====================================================

    if export_type == "assets":

        response = HttpResponse(
            content_type="text/csv"
        )

        response["Content-Disposition"] = (
            'attachment; filename="asetonix_assets.csv"'
        )

        writer = csv.writer(response)

        writer.writerow([
            "ID",
            "Name",
            "Asset Tag",
            "Category",
            "Brand",
            "Model",
            "Serial Number",
            "Purchase Date",
            "Purchase Price",
            "Status",
            "Condition",
            "Location",
            "Notes",
            "Created At",
            "Updated At",
        ])

        assets = Asset.objects.select_related(
            "category",
            "location",
        ).order_by("asset_tag")

        for asset in assets:

            writer.writerow([
                asset.id,
                asset.name,
                asset.asset_tag,
                asset.category.name
                if asset.category else "",
                asset.brand,
                asset.model,
                asset.serial_number,
                asset.purchase_date
                if asset.purchase_date else "",
                asset.purchase_price
                if asset.purchase_price is not None else "",
                asset.get_status_display(),
                asset.get_condition_display(),
                asset.location.name
                if asset.location else "",
                asset.notes,
                asset.created_at,
                asset.updated_at,
            ])

        return response


    # =====================================================
    # ASSIGNMENT DATA EXPORT
    # =====================================================

    if export_type == "assignments":

        response = HttpResponse(
            content_type="text/csv"
        )

        response["Content-Disposition"] = (
            'attachment; filename="asetonix_assignments.csv"'
        )

        writer = csv.writer(response)

        writer.writerow([
            "ID",
            "Asset Tag",
            "Asset Name",
            "Employee ID",
            "Employee Name",
            "Employee Email",
            "Assigned At",
            "Returned At",
            "Assignment Status",
            "Notes",
        ])

        assignments = (
            AssetAssignment.objects
            .select_related(
                "asset",
                "employee",
            )
            .order_by("-assigned_at")
        )

        for assignment in assignments:

            status = (
                "Active"
                if assignment.returned_at is None
                else "Returned"
            )

            writer.writerow([
                assignment.id,
                assignment.asset.asset_tag,
                assignment.asset.name,
                assignment.employee.employee_id,
                assignment.employee.name,
                assignment.employee.email,
                assignment.assigned_at,
                assignment.returned_at
                if assignment.returned_at else "",
                status,
                assignment.notes,
            ])

        return response


    # =====================================================
    # MAINTENANCE DATA EXPORT
    # =====================================================

    if export_type == "maintenance":

        response = HttpResponse(
            content_type="text/csv"
        )

        response["Content-Disposition"] = (
            'attachment; filename="asetonix_maintenance.csv"'
        )

        writer = csv.writer(response)

        writer.writerow([
            "ID",
            "Asset Tag",
            "Asset Name",
            "Title",
            "Description",
            "Priority",
            "Status",
            "Reported At",
            "Started At",
            "Completed At",
            "Cost",
            "Technician",
            "Notes",
        ])

        maintenance_records = (
            MaintenanceRecord.objects
            .select_related("asset")
            .order_by("-reported_at")
        )

        for record in maintenance_records:

            writer.writerow([
                record.id,
                record.asset.asset_tag,
                record.asset.name,
                record.title,
                record.description,
                record.get_priority_display(),
                record.get_status_display(),
                record.reported_at,
                record.started_at
                if record.started_at else "",
                record.completed_at
                if record.completed_at else "",
                record.cost
                if record.cost is not None else "",
                record.technician,
                record.notes,
            ])

        return response


    # =====================================================
    # LIFECYCLE / HISTORY DATA EXPORT
    # =====================================================

    if export_type == "lifecycle":

        response = HttpResponse(
            content_type="text/csv"
        )

        response["Content-Disposition"] = (
            'attachment; filename="asetonix_lifecycle.csv"'
        )

        writer = csv.writer(response)

        writer.writerow([
            "ID",
            "Asset Tag",
            "Asset Name",
            "Event Type",
            "Description",
            "Performed By",
            "Created At",
        ])

        history_records = (
            AssetHistory.objects
            .select_related("asset")
            .order_by("-created_at")
        )

        for history in history_records:

            writer.writerow([
                history.id,
                history.asset.asset_tag,
                history.asset.name,
                history.get_event_type_display(),
                history.description,
                history.performed_by,
                history.created_at,
            ])

        return response


    # =====================================================
    # EXPORT DATA PAGE
    # =====================================================

    return render(
        request,
        "assets/export_data.html",
    )