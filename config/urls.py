from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


urlpatterns = [

    # Django Admin
    path(
        "admin/",
        admin.site.urls
    ),

    # Login
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),

    # Logout
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(
            next_page="/accounts/login/"
        ),
        name="logout",
    ),

    # Asetonix application
    path(
        "",
        include("assets.urls")
    ),
]