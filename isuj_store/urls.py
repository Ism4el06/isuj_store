from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("productos/", include("appProductos.urls")),
    path("admin/", admin.site.urls),
] 