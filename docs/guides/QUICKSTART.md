# Quickstart — integrate Backstage into a Django project

Follow **[INTEGRATION.md](../INTEGRATION.md) first** — it is the single onboarding path. This page adds detail for steps that are easy to get wrong.

## `INSTALLED_APPS` order

**`backstage` must be first.** Contrib sub-apps:

```python
INSTALLED_APPS = [
    "backstage",
    "backstage.contrib.forms",
    "backstage.contrib.inlines",
    "django.contrib.admin",  # after backstage — see reference/AUTO_ADMIN.md
    "django.contrib.auth",
    # ...
    "your_app",
]
```

Why `django.contrib.admin` comes after Backstage: `BackstageConfig.ready()` replaces `admin.site` and registers all models first; your `admin.py` loads later for unregister/re-register overrides.

## Settings import pattern

```python
from yourapp.backstage_host import (
    ADMIN_OVERRIDES,
    FIELD_EDITOR_META,
    MODEL_ICONS,
    MODEL_LABELS,
    NAV_GROUPS,
    TAB_DESCRIPTIONS,
)

BACKSTAGE = {
  # ... see examples/settings_snippet.py
    "PREVIEW_ROUTE_CALLBACK": "yourapp.backstage_host.resolve_preview_route",
}
```

See [examples/settings_snippet.py](../examples/settings_snippet.py) and [reference/CONFIGURATION.md](../reference/CONFIGURATION.md).

## Rich text and TinyMCE

Add a TinyMCE upload route and `django-tinymce`. See [features/EDITOR_UX.md](../features/EDITOR_UX.md).

## Next steps

- Host model conventions: [HOST_CONTRACT.md](HOST_CONTRACT.md)
- Install checklist: [COPY_TO_NEW_PROJECT.md](COPY_TO_NEW_PROJECT.md)
- Return to [INTEGRATION.md](../INTEGRATION.md) for the full narrative.
