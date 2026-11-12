# Install checklist

Use this as a final gate when adding Backstage to a Django project. **Full steps:** [INTEGRATION.md](../INTEGRATION.md).

- [ ] `uv add "django-backstage[tinymce] @ git+https://github.com/JatraTech/django-backstage.git"` (or pinned tag)
- [ ] `backstage` first in `INSTALLED_APPS` (+ contrib apps, then `django.contrib.admin`)
- [ ] `path("backstage/", include("backstage.urls"))` and `path("admin/", admin.site.urls)`
- [ ] `yourapp/backstage_host.py` from [examples/backstage_host.example.py](../examples/backstage_host.example.py)
- [ ] `BACKSTAGE` dict + `PREVIEW_ROUTE_CALLBACK` in settings
- [ ] `python manage.py migrate backstage`
- [ ] `python manage.py check_backstage_integration`
- [ ] Manual QA: [operations/TROUBLESHOOTING.md](../operations/TROUBLESHOOTING.md)

Reference host walkthrough: [django-template](https://github.com/JatraTech/django-template/blob/main/docs/backstage/REFERENCE_HOST.md).
