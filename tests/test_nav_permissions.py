from django.contrib import admin
from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase, override_settings
from django.urls import reverse

from backstage.admin import ModelAdmin
from backstage.nav_permissions import model_for_admin_link, nav_item_allowed, nav_items_any_allowed
from tests.models import NavSampleArticle

User = get_user_model()


class DenyViewAdmin(ModelAdmin):
    def has_view_permission(self, request, obj=None):
        return False


class NavPermissionsModuleTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_model_for_admin_link_changelist(self):
        url = reverse("admin:tests_navsamplearticle_changelist")
        model = model_for_admin_link(admin.site, url)
        self.assertIs(model, NavSampleArticle)

    def test_model_for_admin_link_change(self):
        url = reverse("admin:tests_navsamplearticle_change", args=[1])
        model = model_for_admin_link(admin.site, url)
        self.assertIs(model, NavSampleArticle)

    def test_model_for_admin_link_index_returns_none(self):
        url = reverse("admin:index")
        self.assertIsNone(model_for_admin_link(admin.site, url))

    def test_nav_item_allowed_respects_model_admin_view_permission(self):
        user = User.objects.create_superuser("staff", password="x", email="staff@example.com")
        request = self.factory.get("/admin/")
        request.user = user

        try:
            admin.site.unregister(NavSampleArticle)
        except admin.sites.NotRegistered:
            pass
        admin.site.register(NavSampleArticle, DenyViewAdmin)

        item = {
            "link": reverse("admin:tests_navsamplearticle_changelist"),
            "model": NavSampleArticle,
        }
        self.assertFalse(nav_item_allowed(request, admin.site, item, True))

        admin.site.unregister(NavSampleArticle)
        admin.site.register(NavSampleArticle, ModelAdmin)

    def test_nav_item_allowed_permission_callback_and(self):
        user = User.objects.create_superuser("staff2", password="x", email="staff2@example.com")
        request = self.factory.get("/admin/")
        request.user = user

        item = {
            "link": reverse("admin:tests_navsamplearticle_changelist"),
            "model": NavSampleArticle,
        }
        self.assertTrue(nav_item_allowed(request, admin.site, item, True))
        self.assertFalse(nav_item_allowed(request, admin.site, item, False))

    def test_nav_items_any_allowed_nested(self):
        items = [
            {"has_permission": False, "items": [{"has_permission": True}]},
        ]
        self.assertTrue(nav_items_any_allowed(items))
        self.assertFalse(nav_items_any_allowed([{"has_permission": False}]))


@override_settings(
    BACKSTAGE={
        "NAV_GROUPS": {
            "samples": {
                "title": "Samples",
                "icon": "folder",
                "apps": ["tests"],
                "models": ["tests.NavSampleArticle"],
            },
        },
    }
)
class SidebarPermissionIntegrationTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser("viewer", password="x", email="viewer@example.com")

    def _sample_article_nav_visible(self):
        request = self.factory.get("/admin/")
        request.user = self.user
        groups = admin.site.get_sidebar_list(request)
        for group in groups:
            for item in group.get("items", []):
                if item.get("model") is NavSampleArticle:
                    return item.get("has_permission")
        return None

    def test_sidebar_hides_model_without_view_permission(self):
        try:
            admin.site.unregister(NavSampleArticle)
        except admin.sites.NotRegistered:
            pass
        admin.site.register(NavSampleArticle, DenyViewAdmin)

        self.assertFalse(self._sample_article_nav_visible())

        admin.site.unregister(NavSampleArticle)
        admin.site.register(NavSampleArticle, ModelAdmin)

    def test_sidebar_shows_model_with_view_permission(self):
        self.assertTrue(self._sample_article_nav_visible())

    def test_tabs_list_respects_view_permission(self):
        request = self.factory.get("/admin/")
        request.user = self.user
        tab_link = reverse("admin:tests_navsamplearticle_changelist")

        with override_settings(
            BACKSTAGE={
                "TABS": [
                    {
                        "items": [
                            {
                                "title": "Articles",
                                "link": tab_link,
                                "model": NavSampleArticle,
                            }
                        ]
                    }
                ]
            }
        ):
            try:
                admin.site.unregister(NavSampleArticle)
            except admin.sites.NotRegistered:
                pass
            admin.site.register(NavSampleArticle, DenyViewAdmin)
            tabs = admin.site.get_tabs_list(request)
            self.assertFalse(tabs[0]["items"][0]["has_permission"])
            admin.site.unregister(NavSampleArticle)
            admin.site.register(NavSampleArticle, ModelAdmin)
