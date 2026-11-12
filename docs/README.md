# Backstage documentation

Backstage is a self-contained Django admin package. Host projects add models; Backstage auto-registers them with shared changelist, change forms, navigation, preview, and editor metadata.

**Start here:** **[INTEGRATION.md](INTEGRATION.md)** — single onboarding path (`backstage_host.py`).

Package source: [github.com/JatraTech/django-backstage](https://github.com/JatraTech/django-backstage).

## Documentation layout

```text
README.md              # Package entry (repo root)
docs/README.md         # This index
docs/INTEGRATION.md    # Onboarding spine (start here)
docs/guides/           # SCREAMING_SNAKE.md (how-to)
docs/features/         # SCREAMING_SNAKE.md (behavior)
docs/reference/        # SCREAMING_SNAKE.md (+ config-keys.yaml)
docs/operations/       # SCREAMING_SNAKE.md (runbooks)
docs/examples/         # Copy-paste host snippets (*.py); examples/README.md
docs/CHANGELOG.md      # Release notes
```

**Naming:** Every topic markdown under `docs/` (including subfolders) uses **SCREAMING_SNAKE.md** (`EDITOR_UX.md`, `HOST_CONTRACT.md`). Hyphens in the old kebab names become underscores. Keep `README.md` and `CHANGELOG.md` as-is. Code under `docs/examples/*.py` stays lowercase.

## Reading order

| Step | Document | When to read |
|------|----------|--------------|
| 1 | [INTEGRATION.md](INTEGRATION.md) | **Start here** — install, `backstage_host.py`, settings |
| 2 | [guides/QUICKSTART.md](guides/QUICKSTART.md) | `INSTALLED_APPS` order and settings detail |
| 3 | [guides/HOST_CONTRACT.md](guides/HOST_CONTRACT.md) | CMS model conventions |
| 4 | [reference/CONFIGURATION.md](reference/CONFIGURATION.md) | Every `BACKSTAGE` key |
| 5 | [reference/AUTO_ADMIN.md](reference/AUTO_ADMIN.md) | Autodiscover and factory |
| 6 | [features/CUSTOMIZATION.md](features/CUSTOMIZATION.md) | Overrides |
| 7 | [features/PREVIEW_AND_FRONTEND.md](features/PREVIEW_AND_FRONTEND.md) | Preview + API |
| 8 | [features/EDITOR_UX.md](features/EDITOR_UX.md) | Editor meta policy |
| 9 | [operations/TROUBLESHOOTING.md](operations/TROUBLESHOOTING.md) | Failures and manual QA |
| 10 | [features/DRAFT_PUBLISH.md](features/DRAFT_PUBLISH.md) | Draft rows + preview |
| 11 | [guides/COPY_TO_NEW_PROJECT.md](guides/COPY_TO_NEW_PROJECT.md) | Final install checklist |
| — | [CHANGELOG.md](CHANGELOG.md) | Package release history |

Host config example — copy from `docs/examples/backstage_host.example.py`:

```bash
cp docs/examples/backstage_host.example.py yourapp/backstage_host.py
```

## Verification

```bash
python manage.py check_backstage_integration
```

| Term | Meaning |
|------|---------|
| **Backstage** | The `backstage` Django app in this package |
| **Host project** | Your Django project apps |
| **`backstage_host.py`** | Single host config module (nav, overrides, editor meta, preview) |
| **`BACKSTAGE`** | Settings dict merged with package defaults |
| **Admin appearance** | DB-backed branding singleton |

## Host module checklist

| Export | Purpose |
|--------|---------|
| `NAV_GROUPS`, `MODEL_ICONS`, `MODEL_LABELS` | Sidebar |
| `ADMIN_OVERRIDES` | Per-model admin attrs |
| `FIELD_EDITOR_META`, `TAB_DESCRIPTIONS` | Editor UX |
| `resolve_preview_route` | Preview iframe paths |

Wire in `settings.py`; set `PREVIEW_ROUTE_CALLBACK` to `"yourapp.backstage_host.resolve_preview_route"`.
