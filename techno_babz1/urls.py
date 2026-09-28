"""
URL configuration for techno_babz1 project.

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

from .sitemaps import StaticViewSitemap


sitemaps = {
    "static": StaticViewSitemap,
}


urlpatterns = [
    path("admin/", admin.site.urls),

    path("", include("home.urls")),

    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="sitemap",
    ),
]