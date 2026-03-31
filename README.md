# FixMyCommunity

A user-centered Django web application that improves communication, issue reporting, progress tracking, and access to reliable local information for residents in communities.

 Overview

**FixMyCommunity** is a system designed to address the challenges residents face in reporting and tracking service delivery issues such as:
-  Water leaks
- Electricity faults
-  Potholes
-  Waste collection problems

The platform provides a straightforward, interactive system that enhances communication between communities and service providers.

## Project Structure

```
FixMyCommunity/
├── fixmycommunity_config/      # Main Django project config
│   ├── settings.py              # Project settings
│   ├── urls.py                  # URL routing configuration
│   └── wsgi.py                  # WSGI application
├── issues/                       # Issues app - for reporting service issues
│   ├── migrations/              # Database migrations
│   ├── templates/
│   │   └── issues/
│   │       ├── issue_list.html  # Display all reported issues
│   │       └── issue_detail.html # Single issue details
│   ├── models.py                # Issue model definition
│   ├── views.py                 # Issue views (list & detail)
│   ├── urls.py                  # Issue URL patterns
│   └── admin.py                 # Django admin configuration
├── communities/                  # Communities app - for community info & tracking
│   ├── migrations/              # Database migrations
│   ├── templates/
│   │   └── communities/
│   │       ├── communities_list.html    # Display all communities
│   │       └── community_detail.html    # Single community details
│   ├── models.py                # Community model definition
│   ├── views.py                 # Community views (list & detail)
│   ├── urls.py                  # Community URL patterns
│   └── admin.py                 # Django admin configuration
├── manage.py                     # Django management script
├── README.md                     # This file
└── env/                          # Virtual environment
```

##  Apps Overview

### 1. **Issues App**
Handles the reporting and tracking of service delivery issues.

**Models:**
- `Issue`: Stores information about reported issues
  - Issue type (water leak, electricity fault, pothole, waste collection)
  - Status (reported, in progress, resolved, rejected)
  - Priority level
  - Location and reporter information
  - Timestamps and image attachments

**Views:**
- `issues_list`: Display all issues with filtering capabilities
- `issue_detail`: Show detailed information about a specific issue

**Features:**
- Filter by status, type, and priority
- Track issue progress
- View reporter information

### 2. **Communities App**
Manages community information and provides access to reliable local data.

**Models:**
- `Community`: Stores community information
  - Contact details
  - Location
  - Total residents
  - Activation status

**Views:**
- `communities_list`: Display all active communities with issue statistics
- `community_detail`: Show community information and related issues

**Features:**
- View community details
- Track issue resolution progress by community
- Access contact information
- View statistics on reported and resolved issues

### Prerequisites
- Python 3.8+
- Django 6.0.3+
- pip

### Installation

1. **Clone the repository** (or navigate to the project directory)
   ```bash
   cd FixMyCommunity
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser** (for admin access)
   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Web Interface: http://127.0.0.1:8000/
   - Issues Page: http://127.0.0.1:8000/issues/
   - Communities Page: http://127.0.0.1:8000/communities/
   - Admin Panel: http://127.0.0.1:8000/admin/

##  URL Patterns

### Issues App (`/issues/`)
- `/issues/` - List all reported issues
- `/issues/<issue_id>/` - View issue details

### Communities App (`/communities/`)
- `/communities/` - List all communities with statistics
- `/communities/<community_id>/` - View community details and related issues

### Admin
- `/admin/` - Django administration panel

## Database Models

### Issue Model
```python
- title: CharField (max 200)
- description: TextField
- issue_type: CharField (water_leak, electricity, pothole, waste, other)
- location: CharField (max 300)
- status: CharField (reported, in_progress, resolved, rejected)
- priority: IntegerField (1=Low, 2=Medium, 3=High)
- reporter_name: CharField
- reporter_email: EmailField
- image: ImageField (optional)
- created_at: DateTimeField (auto)
- updated_at: DateTimeField (auto)
```

### Community Model
```python
- name: CharField (unique, max 200)
- description: TextField
- location: CharField (max 300)
- contact_person: CharField (max 150)
- contact_email: EmailField
- contact_phone: CharField (max 20)
- total_residents: IntegerField
- active: BooleanField
- created_at: DateTimeField (auto)
- updated_at: DateTimeField (auto)
```

##  Features

 **Issue Reporting** - Users can view all reported issues
 **Community Information** - Access local community details
 **Progress Tracking** - Monitor issue resolution status
 **Filtering & Search** - Filter issues by type, status, and priority
 **Statistics** - View community issue statistics
 **Admin Panel** - Manage issues and communities through Django admin
**Responsive Design** - Modern, user-friendly interface

##  Security Notes

- Change `SECRET_KEY` in settings.py before production deployment
- Set `DEBUG = False` in production
- Configure `ALLOWED_HOSTS` appropriately
- Use HTTPS in production
- Store sensitive data in environment variables

## Technologies Used

- **Backend**: Django 6.0.3
- **Database**: SQLite (default, easily switched to PostgreSQL/MySQL)
- **Frontend**: HTML5, CSS3
- **Python**: 3.14.3

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

##  GitHub Repository

**[GitHub Link: FixMyCommunity](https://github.com/yourusername/FixMyCommunity)**

*Note: Replace `yourusername` with your actual GitHub username when you create the repository.*

### To Initialize Git and Push to GitHub:

```bash
# Initialize git repository
git init
git add .
git commit -m "Initial commit: FixMyCommunity Django project"

# Add remote and push
git remote add origin https://github.com/yourusername/FixMyCommunity.git
git branch -M main
git push -u origin main
```

##  Support & Contact

For issues, questions, or suggestions, please:
- Create an issue on GitHub
- Contact the development team
- Email: support@fixmycommunity.local


