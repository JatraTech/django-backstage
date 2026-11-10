# django-backstage

Backstage admin theme for Django: custom `AdminSite`, sidebar navigation, dashboard widgets, draft/preview hooks, and host-driven `BACKSTAGE` configuration.

Source: [github.com/JatraTech/django-backstage](https://github.com/JatraTech/django-backstage).

## Install

In another project:

```text
uv add "django-backstage[tinymce] @ git+https://github.com/JatraTech/django-backstage.git"
```

A specific branch or tag:

```text
uv add "django-backstage[tinymce] @ git+https://github.com/JatraTech/django-backstage.git@v0.1.0"
```

In this repo:

```text
uv sync --all-extras --group dev
uv run pytest
```

pip fallback: `pip install -e ".[all]"`.

| Extra | Adds |
|---|---|
| `tinymce` | `django-tinymce` (rich-text admin mixins) |
| `all` | Same as `tinymce` |
| `test` | pytest, pytest-django, django-tinymce |

## Host project wiring

`backstage` must be **first** in `INSTALLED_APPS` (it replaces `admin.site` on startup).

```python
INSTALLED_APPS = [
    "backstage",
    "backstage.contrib.forms",
    "backstage.contrib.inlines",
    "django.contrib.admin",  # after backstage
    # your apps
]

MIDDLEWARE = [
    # ...
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "backstage.middleware.AdminRequestMiddleware",
    # ...
]

urlpatterns = [
    path("backstage/", include("backstage.urls")),
    path("admin/", admin.site.urls),
]
```

```bash
python manage.py migrate backstage
python manage.py check_backstage_integration
```

Add `yourapp/backstage_host.py` (navigation, `ADMIN_OVERRIDES`, `FIELD_EDITOR_META`, preview route callback) and merge exports into `settings.BACKSTAGE`. The package does not ship host-specific nav.

Rich text: install the `tinymce` extra and wire TinyMCE URLs/upload JS in the host (see integration docs in the django-template reference host).

## Upgrades

After bumping the package version, run:

```bash
python manage.py migrate backstage
```
