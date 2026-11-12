from django.contrib import admin
from django.urls import include, path

from backstage.views import tinymce_upload

urlpatterns = [
    path("admin/tinymce/upload/", tinymce_upload, name="tinymce_upload"),
    path("admin/", admin.site.urls),
    path("backstage/", include("backstage.urls")),
]
