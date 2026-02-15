# Devread - Book Review Platform

A Django-based web application for sharing and discovering book reviews. Users can browse books, read reviews, and share their own reading experiences with the community.

## Features

- **User Authentication**: Email-based authentication system with secure password management
- **Book Management**: Browse books organized by categories and authors
- **Reviews**: Read and write detailed reviews for books
- **User Profiles**: Manage personal profile information and avatar
- **Category Browsing**: Explore books by categories
- **Responsive Design**: Mobile-friendly interface

## Tech Stack

- **Backend**: Django 6.0+
- **Database**: SQLite
- **Python**: 3.13+
- **Frontend**: HTML5, CSS, JavaScript
- **Package Manager**: uv

## Project Structure

```
devread/
├── devread_core/          # Main Django project settings
│   ├── templates/         # HTML templates
│   ├── static/            # CSS, JavaScript, images
│   └── settings.py        # Project configuration
├── accounts/              # User authentication & profiles
├── books/                 # Books, authors, categories
├── reviews/               # Book reviews functionality
├── home/                  # Homepage
├── media/                 # User-uploaded files (avatars, etc)
├── manage.py              # Django management script
├── pyproject.toml         # Project dependencies
└── db.sqlite3             # SQLite database
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd devread
   ```

2. **Set up Python environment**:
   ```bash
   uv venv
   source .venv/Scripts/activate  # Windows
   # or
   source .venv/bin/activate     # macOS/Linux
   ```

3. **Install dependencies**:
   ```bash
   uv sync
   ```

4. **Apply database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

## Running the Project

Start the development server:
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000/`

## Running Tests

Run all tests:
```bash
python manage.py test
```

Run tests for a specific app:
```bash
python manage.py test accounts
python manage.py test books
python manage.py test reviews
python manage.py test home
```

## Database Management

Make migrations:
```bash
python manage.py makemigrations
```

Apply migrations:
```bash
python manage.py migrate
```

## Apps Overview

### accounts
User authentication and profile management
- Custom User model (extends Django's AbstractUser)
- Email-based authentication
- User profiles with avatars

### books
Book catalog management
- Book model with slug field for URLs
- Author model
- Category model
- Search and filtering functionality

### reviews
Book review functionality
- Review creation and management
- Review ratings and comments
- User review history

### home
Homepage and main navigation
- Landing page
- Featured books section
- Navigation menu

## Configuration

- **Templates**: `devread_core/templates/`
- **Static Files**: `devread_core/static/`
- **Media Uploads**: `media/` directory
- **Settings**: `devread_core/settings.py`

## Development Guidelines

- **Python**: Use type hints in new code
- **Code Style**: Follow Django conventions and PEP 8
- **Indentation**: 4 spaces
- **Models**: Use `slug` fields for URLs, `auto_now_add=True` for creation timestamps
- **Error Handling**: Use Django's ValidationError for model validation
- **Imports**: Django imports first, then standard library, then app imports

## Admin Interface

Access the Django admin panel at:
```
http://localhost:8000/admin/
```

Use the superuser credentials you created during installation.



## License

MIT License


