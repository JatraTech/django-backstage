from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings


@override_settings(
    MEDIA_ROOT="/tmp/backstage-test-media",
    STORAGES={
        "default": {"BACKEND": "django.core.files.storage.FileSystemStorage"},
        "staticfiles": {"BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"},
    },
)
class TinymceUploadTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.staff = User.objects.create_user(username="editor", password="pw", is_staff=True)
        self.client = Client()
        self.client.force_login(self.staff)

    def test_staff_image_upload_returns_location(self):
        image = SimpleUploadedFile("tiny.png", b"\x89PNG\r\n\x1a\n", content_type="image/png")
        response = self.client.post("/admin/tinymce/upload/", {"file": image})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("location", data)
        self.assertTrue(data["location"])

    def test_rejects_non_image(self):
        doc = SimpleUploadedFile("notes.txt", b"hello", content_type="text/plain")
        response = self.client.post("/admin/tinymce/upload/", {"file": doc})
        self.assertEqual(response.status_code, 400)

    def test_anonymous_redirected(self):
        client = Client()
        image = SimpleUploadedFile("tiny.png", b"\x89PNG\r\n\x1a\n", content_type="image/png")
        response = client.post("/admin/tinymce/upload/", {"file": image})
        self.assertIn(response.status_code, (302, 403))
