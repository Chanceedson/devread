# Devread Project Guide

## Build & Test Commands
- **Run server**: `python manage.py runserver`
- **Run tests**: `python manage.py test`
- **Run single app tests**: `python manage.py test accounts` (or `books`, `reviews`, `home`)
- **Make migrations**: `python manage.py makemigrations`
- **Apply migrations**: `python manage.py migrate`

## Architecture
Django 6.0+ project with SQLite database (db.sqlite3). Core project in `devread_core/`. Custom Django apps:
- `accounts`: User model (extends AbstractUser, email-based auth)
- `books`: Books, Authors, Categories models with slug fields
- `reviews`: Book reviews
- `home`: Homepage

Template root: `devread_core/templates/`, static files in `devread_core/static/`, media uploads to `media/`.

## Code Style
- Python 3.13+, use type hints in new code
- Django conventions: models in models.py, views in views.py, tests in tests.py
- 4-space indentation, follow Django's coding style guide
- Models: use `slug` fields for URLs, `auto_now_add=True` for creation timestamps, `auto_now=True` for updates
- Error handling: use Django's ValidationError for model validation
- Imports: Django imports first, then standard library, then app imports
