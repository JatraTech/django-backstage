from django.urls import path

from backstage.tinymce_upload import tinymce_upload

urlpatterns = [
    path("upload/", tinymce_upload, name="tinymce_upload"),
]
