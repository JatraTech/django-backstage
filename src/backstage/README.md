# Backstage Admin Panel

Django admin UI for host projects: auto-registration, shared changelist and change forms, navigation, preview, and editor metadata.

## Documentation

**Canonical docs:** [github.com/JatraTech/django-backstage/tree/main/docs](https://github.com/JatraTech/django-backstage/tree/main/docs) — start with [integration.md](https://github.com/JatraTech/django-backstage/blob/main/docs/integration.md).

## Install (minimal)

```python
INSTALLED_APPS = [
    "backstage",
    "backstage.contrib.forms",
    "backstage.contrib.inlines",
    "django.contrib.admin",  # after backstage
    # ... your apps
]
```

```bash
python manage.py migrate backstage
python manage.py check_backstage_integration
```

Branding: **System → Admin appearance** (DB overrides `BACKSTAGE`).

## Inline relations (host config)

Declare parent → child edges in `BACKSTAGE["INLINE_RELATIONS"]` (compiled at startup into inlines, `STANDALONE_CHILD_MODELS`, and child `exclude` as needed):

| `mode` | Behavior |
|--------|----------|
| `default_stacked` | Editable stacked inline (factory default if omitted) |
| `default_tabular` | Editable tabular inline |
| `hub_tabular` / `hub_stacked` | Read-only summary + Edit/Delete + Add/View all footer; default **primary tab** with parent fieldset tabs |

Legacy `INLINE_HUB` + manual `ADMIN_OVERRIDES.inlines` still work; prefer `INLINE_RELATIONS` for new hosts. Escape hatch: `inline_class` dotted path on a relation entry.

Stacked inline “Add another …” labels use the child model’s `Meta.verbose_name` on factory-built inlines.

## Package layout

```
backstage/
  apps.py              # Admin site + autodiscover
  registry/            # factory, navigation, editor meta
  preview/             # tokens, routes, DRF mixin
  templates/           # Admin UI
  static/backstage/    # CSS, JS, preview
```
