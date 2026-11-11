# Backstage docs changelog

## 2026-11-10 (docs on package repo)

- Canonical Backstage manual lives in **`django-backstage/docs/`**.

## 2026-11-10 (installable package)

- **django-backstage:** Backstage admin ships as [JatraTech/django-backstage](https://github.com/JatraTech/django-backstage) (`uv add` git dependency). After install, run `migrate backstage` and wire `backstage_host.py` / `BACKSTAGE` in your project.

## 2026-10-30 (admin activity log)

- **Admin activity log:** Dashboard Recent activity shows change summaries, IP (when captured), and superuser-wide feed; **System → Admin activity** read-only changelist (action type, Open link, filters). Migrations `0004_adminlogentrymeta`, `0005_adminactivitylog`.
- **Host wiring:** Add `backstage.middleware.AdminRequestMiddleware` after auth; optional `BACKSTAGE["TRUSTED_PROXY_COUNT"]` (env) for production client IP behind nginx; allowlist `backstage.AdminActivityLog` in `NAV_GROUPS["system"].models`.
- **Upgrades:** Pin `django-backstage`, run `migrate backstage`, add middleware + nav + env in `backstage_host.py` as needed.

## 2026-10-23 (sidebar permissions)

- **Sidebar and tabs:** Nav items respect `ModelAdmin.has_view_permission` (same as Django app list and dashboard widgets). Auto-built `NAV_GROUPS` items include a `model` reference; manual `SIDEBAR.navigation` entries can set `"model"` or rely on admin URL resolution.
- **Empty groups:** Sidebar groups with no permitted items are omitted server-side.

## 2026-10-23 (custom admins and nav tabs)

- **Changelist row actions:** `backstage.admin.ModelAdmin` defaults `changelist_row_edit` and `changelist_row_delete` to `True` so custom admins match autodiscovered behavior.
- **Admin appearance:** `custom_css` on Backstage settings uses `BackstageAdminTextareaWidget` (consistent padding with other admin textareas).
- **Sidebar tab highlight:** `_admin_path_matches` compares tab link query strings via `request_query` (fixes active nav when change-form tabs use `?tab=…`).
- **Docs:** Troubleshooting for raw Django widgets and primary link buttons in changelists; `host_admin_utils.example.py` for unregister/re-register patterns.

## 2026-10-02 (changelist and favicon)

- **Changelist bulk actions:** Django-style always-visible action row (select + Go + selection counter); compact toolbar CSS; slightly taller table rows.
- **Admin tab icon:** Auto-generates letterboxed 32×32 PNG `favicon_light` from `logo_light` on save (helper in `backstage.favicon_images`); migration `0003_backstagesettings_favicon_light` backfills existing logos on upgrade.

## 2026-10-02 (favicon CLI removed)

- Removed `regenerate_admin_favicon` management command; favicon updates happen on `logo_light` save or via migration `0003` only.

## 2026-10-02 (package sync)

- **Hub inlines:** `INLINE_RELATIONS` compiler, `primary_tab_slug` (hub tab merged into parent fieldset tabs), scrollable fieldset tabs with horizontal wheel scroll.
- **Branding:** `branding_defaults_from_config()` seeds new `BackstageSettings` rows; migration `0002_backfill_branding_from_config` one-time backfill from `BACKSTAGE` SITE_* when DB fields are empty; display uses DB only via `resolve_branding_field` / `resolve_text` (cleared fields stay empty).
- **Admin UX:** Image preview checkerboard/border styling; dashboard welcome title respects resolved site header.

## 2026-10-02 (earlier note — superseded)

- The short-lived doc set that removed hub/`INLINE_RELATIONS` is **superseded** by the package sync above. Prefer `INLINE_RELATIONS` for parent→child edges; use `ADMIN_OVERRIDES` for one-off tweaks.

## 2026-09-29

- **INLINE_RELATIONS** and hub inline modes added to the package.
