# Release Management Dashboard
Django 5.x application managing release metadata (Roles, Employees, Customers, Projects, Versions, Locations, Coordination & Execution Escalations, Contact submissions) with prototype access control and backup utilities.

## Table of Contents
Overview | Features | Structure | Installed Apps | Prerequisites | Data Model | Access Control | Templates | Validation | Backup & Restore | CSV Export | Environment | Quick Start | Commands | Migrations | Testing | Static Files | Security | Roadmap | Known Issues | Contributing | License

## Overview
Provides CRUD, CSV export, incremental table backups, and provisional session‑flag access control (to be replaced by Django permissions).

## Features
Current:
- CRUD for principal domain entities.
- Session flags: can_view/add/edit/delete/export.
- Central base + navigation templates.
- Custom 404 (active when DEBUG=False).
- Incremental backup script (hash comparison).
- CSV export endpoints.
Planned:
- Auth + groups/permissions.
- DRF API.
- Server‑side pagination & search.
- Backup rotation + restore command.
- Composite uniqueness for Version (project + operation_system + version).
- Structured logging & audit trail.
- Centralized validators.

## Directory Structure
```
manage.py
Main/
Role/ Employee/ Customer/ Project/ Version/
Location/ Coordination_and_Execution_Escalation/ ContactUs/
AccessControl_Role/ AccessControl_Employee/
templates/ static/ SamplePages/
table_backups/
backup_all_tables.py
requirements.txt
ReadMe.md
URL_CONFIGURATION.md
```

## Installed Apps
Configured in Main/settings.py. Domain apps + access control scaffolds (AccessControl_Role, AccessControl_Employee).

## Prerequisites
Python 3.12+, pip, virtual environment recommended, Git.

## Data Model
- Project: unique integer code, name, description.
- Version: FK project, operation_system, version string, unique policy_name, optional confluence_page_link.
- Escalation: FK employee, location (see initial migration).
- Backup metadata: table_backups/current/backup_info.txt.

### Composite Uniqueness (Version) (Recommended)
Add Meta:
```python
class Meta:
    db_table = 'versions'
    ordering = ['project', 'operation_system', 'version']
    indexes = [
        models.Index(fields=['policy_name']),
        models.Index(fields=['project', 'operation_system', 'version']),
    ]
    constraints = [
        models.UniqueConstraint(
            fields=['project','operation_system','version'],
            name='unique_project_os_version'
        ),
    ]
```
Then:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Access Control
access_required + Check_access (Main/auth_utils.py) populate session flags used by templates to show/hide actions. Replace with Django permissions.

## Templates
Base/top navigation: templates/top.html, templates/menu.html. Per‑app folders under templates/<AppName>/. Access control templates under templates/AccessControl_* . SamplePages static reference only.

## Validation
Forms implement clean_<field>. Recommendation: centralize regex (version pattern, phone, URL) in helper module to avoid duplication.

## Backup & Restore
Script: backup_all_tables.py
- Hash each table; write changed tables to table_backups/current/.
- last_backup_hashes.json tracks previous state.
Run:
```bash
python backup_all_tables.py
```
Planned: timestamped dirs, rotation, restore utility, integrity manifest.

## CSV Export
Guarded by session flag can_export; uses csv.writer and attachment headers.

## Environment & Settings
Use .env with python-decouple or django-environ.
Example .env:
```
DJANGO_SECRET_KEY=change-me
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```
Add .env.example for onboarding.

## Quick Start
```bash
python -m venv .venv
# Windows:
.\.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Create superuser:
```bash
python manage.py createsuperuser
```

## Common Commands
```bash
python manage.py showmigrations
python manage.py collectstatic
python manage.py check --deploy
python manage.py shell
```

## Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
Dev reset (Windows):
```powershell
del db.sqlite3
python manage.py migrate
```

## Testing
Focus: form validation edge cases, access flag propagation, backup idempotence. Run:
```bash
python manage.py test
```

## Static Files (Production)
1. DEBUG=False
2. Set ALLOWED_HOSTS
3. Collect:
```bash
python manage.py collectstatic
```
4. Serve via WhiteNoise or external web server.

## Security
- Move SECRET_KEY to .env.
- Enforce composite uniqueness on Version.
- Transition to permissions/groups.
- Sanitize external URLs.
- Implement pagination for large lists.
- Add audit logging (model signals).
- Regenerate requirements.txt if malformed.

## Development Roadmap
1. Django auth integration
2. Permission system migration
3. Composite Version uniqueness
4. Shared validators module
5. DRF read-only API endpoints
6. Server-side pagination/search
7. Backup rotation & restore
8. Test coverage expansion
9. Structured logging + auditing

## Known Issues
- ContactUs vs ContactUS naming (standardize to ContactUs; adjust imports/settings).
- Version collisions possible without composite constraint (policy_name alone insufficient).
- Potential malformed requirements.txt (null separators) → regenerate with pip freeze.
- Duplicate regex rules in forms.
- Restore procedure undocumented.
- Session flags may default permissively.

## Contributing
Fork → branch → changes → tests → pull request.

## License
Internal use (Release Management Team @ Lumen). Add LICENSE file if distribution scope changes.