from django.urls import path

from .views import dashboard, assets_list


urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("assets/", assets_list, name="assets_list"),
]