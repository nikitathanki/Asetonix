from django.urls import path

from .views import (
    dashboard,
    assets_list,
    asset_detail,
    assign_asset,
    transfer_asset,
)


urlpatterns = [
    path(
        "",
        dashboard,
        name="dashboard",
    ),

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
]