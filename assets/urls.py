from django.urls import path

from .views import (
    dashboard,
    assets_list,
    asset_detail,
    assign_asset,
    transfer_asset,
    report_maintenance,
    maintenance_list,
    assignments_list,
    transfers_list,
    retirements_list,
    retire_asset,
    asset_health,
    utilization,
    risk_analysis,
    cost_analysis,
    audit_trail,
    categories,
    brands,
    models_list,
    departments,
    locations,

)


urlpatterns = [

    # =====================================================
    # DASHBOARD
    # =====================================================

    path(
        "",
        dashboard,
        name="dashboard",
    ),


    # =====================================================
    # ASSETS
    # =====================================================

    path(
        "assets/",
        assets_list,
        name="assets_list",
    ),

    path(
        "assets/<str:asset_tag>/",
        asset_detail,
        name="asset_detail",
    ),


    # =====================================================
    # ASSET ACTIONS
    # =====================================================

    path(
        "assets/<str:asset_tag>/assign/",
        assign_asset,
        name="assign_asset",
    ),

    path(
        "assets/<str:asset_tag>/transfer/",
        transfer_asset,
        name="transfer_asset",
    ),

    path(
        "assets/<str:asset_tag>/maintenance/",
        report_maintenance,
        name="report_maintenance",
    ),

    path(
        "assets/<str:asset_tag>/retire/",
        retire_asset,
        name="retire_asset",
    ),


    # =====================================================
    # MANAGEMENT LISTS
    # =====================================================

    path(
        "maintenance/",
        maintenance_list,
        name="maintenance_list",
    ),

    path(
        "assignments/",
        assignments_list,
        name="assignments_list",
    ),

    path(
        "transfers/",
        transfers_list,
        name="transfers_list",
    ),

    path(
        "retirements/",
        retirements_list,
        name="retirements_list",
    ),
    path(
    "asset-health/",
    asset_health,
    name="asset_health",
    ),
    path(
    "utilization/",
    utilization,
    name="utilization",
    ),

    path(
    "risk-analysis/",
    risk_analysis, 
    name="risk_analysis"
    ),


    path(
        "cost-analysis/",
        cost_analysis,
        name="cost_analysis",
    ),

    path(
    "audit-trail/",
    audit_trail,
    name="audit_trail",
    ),

    path(
    "categories/",
    categories,
    name="categories",
    ),

    path(
    "brands/",
    brands,
    name="brands",
    ),

    path(
    "models/",
    models_list,
    name="models",
    ),

    path(
    "departments/",
    departments,
    name="departments",
    ),

    path(
    "locations/",
    locations,
    name="locations",
    ),

]