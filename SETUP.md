# FixMyCommunity Project Setup Guide

## Quick Start Guide

Follow these steps to get FixMyCommunity running on your local machine.

### 1. Prerequisites

- Python 3.8 or higher
- Git (for cloning the repository)
- pip (Python package installer)

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/FixMyCommunity.git
cd FixMyCommunity
```

### 3. Create Virtual Environment

```bash
# Windows
python -m venv env
env\Scripts\activate

# macOS/Linux
python3 -m venv env
source env/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin user:
- Username: (e.g., admin)
- Email: (e.g., admin@fixmycommunity.local)
- Password: (choose a strong password)

### 7. Run Development Server

```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

### 8. Access the Application

- **Home**: http://127.0.0.1:8000/
- **Issues List**: http://127.0.0.1:8000/issues/
- **Communities List**: http://127.0.0.1:8000/communities/
- **Admin Panel**: http://127.0.0.1:8000/admin/

## Project Structure Overview

### Main Project (`fixmycommunity_config/`)
- Central Django configuration
- URL routing
- Settings management

### Issues App (`issues/`)
**Purpose**: Handle service issue reporting and tracking

**Files**:
- `models.py` - Issue model with fields for tracking problems
- `views.py` - Views for listing and details
- `urls.py` - URL patterns
- `admin.py` - Django admin configuration
- `templates/` - HTML templates for display

**Features**:
- Report issues (water leaks, electricity faults, potholes, waste)
- Filter by status, type, and priority
- Track resolution progress
- View issue details and reporter information

### Communities App (`communities/`)
**Purpose**: Manage community information and progress tracking

**Files**:
- `models.py` - Community model
- `views.py` - Views for communities
- `urls.py` - URL patterns
- `admin.py` - Django admin configuration
- `templates/` - HTML templates

**Features**:
- List all active communities
- View community details
- Track issues per community
- Show issue statistics (reported, in progress, resolved)

## Database Models

### Issue Model
Stores service delivery issues with the following fields:
- Title, Description, Type, Location
- Status (reported, in progress, resolved, rejected)
- Priority level (1-3)
- Reporter name and email
- Optional image attachment
- Timestamps (created_at, updated_at)

### Community Model
Stores community information with fields:
- Name, Description, Location
- Contact person, email, phone
- Total residents count
- Active status
- Timestamps

## Important Files

- `requirements.txt` - All Python dependencies
- `.gitignore` - Git ignore patterns
- `manage.py` - Django management script
- `README.md` - Project overview

## Common Commands

```bash
# Run development server
python manage.py runserver

# Create migrations for changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Run system checks
python manage.py check

# Create superuser
python manage.py createsuperuser

# Django shell
python manage.py shell

# Collect static files (production)
python manage.py collectstatic

# Create backup
python manage.py dumpdata > backup.json

# Load backup
python manage.py loaddata backup.json
```

## Adding Sample Data via Admin Panel

1. Go to http://127.0.0.1:8000/admin/
2. Log in with your superuser credentials
3. Click on "Communities" to add a community
4. Click on "Issues" to add issues
5. Fill in the form fields and save

## Architecture Overview

```
User Interface (HTML/CSS)
        ↓
Django Views (issues/communities views)
        ↓
Models (Issue, Community)
        ↓
SQLite Database
```

## Troubleshooting

### Port Already in Use
```bash
python manage.py runserver 8001
```

### Database Locked Error
```bash
# Remove the database and migrate again
rm db.sqlite3
python manage.py migrate
```

### Module Not Found
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### Static Files Not Loading
```bash
# Collect static files
python manage.py collectstatic --noinput
```

## Deployment Considerations

Before deploying to production:

1. **Change SECRET_KEY** in `settings.py`
2. **Set DEBUG = False** in `settings.py`
3. **Configure ALLOWED_HOSTS** with your domain
4. **Use environment variables** for sensitive data
5. **Set up a production database** (PostgreSQL recommended)
6. **Use HTTPS/SSL certificate**
7. **Configure CSRF trusted origins**
8. **Set up proper logging**
9. **Use a production WSGI server** (Gunicorn recommended)

## Development Workflow

1. Create a new branch for features
2. Make changes and test locally
3. Run `python manage.py check` to verify
4. Commit and push to GitHub
5. Create a pull request for review

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Models](https://docs.djangoproject.com/en/6.0/topics/db/models/)
- [Django Views](https://docs.djangoproject.com/en/6.0/topics/http/views/)
- [Django Templates](https://docs.djangoproject.com/en/6.0/topics/templates/)
- [Django Admin](https://docs.djangoproject.com/en/6.0/ref/contrib/admin/)

## Support

For issues or questions:
- Check the README.md file
- Review the Django documentation
- Create an issue on GitHub
- Contact the development team

---

**Happy coding! 🚀**
