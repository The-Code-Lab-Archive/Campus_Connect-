# Campus Connect - Backend (Django REST API)
Backend URL:
https://campus-connect-0s5h.onrender.com/
## Overview
Django REST API backend for Campus Connect, a comprehensive web platform for University of Arkansas students to discover campus events, join student organizations, and access AI assistance.

## What It Does
Campus Connect backend provides a robust Django REST API that manages:
- **Events Management**: Store and organize campus events with details like title, description, date, time, location, and categories
- **Organizations System**: Manage student organizations with member tracking, categorization, and organization details
- **User Authentication**: Handle user accounts with custom user models for profile management
- **Blog & News**: Maintain a campus blog system for announcements and updates
- **Admin Interface**: Provide a powerful admin panel for content management and moderation
- **Database Operations**: Perform complete CRUD operations through Django's ORM
- **API Ready**: Configured with Django REST Framework and CORS for frontend integration

## Tech Stack
- **Framework**: Django 5.x
- **API**: Django REST Framework
- **Database**: SQLite (development)
- **CORS**: django-cors-headers
- **Admin Panel**: Django Admin

## Project Structure
```
campus-connect/
└── backend/                     # Backend folder
    ├── campus_connect/          # Main project settings
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── blog/                    # Blog app
    ├── events/                  # Events management app
    ├── organizations/           # Student organizations app
    ├── users/                   # User authentication & profiles
    ├── manage.py
    └── db.sqlite3              # SQLite database
```

## Setup & Installation

### Prerequisites
- Python 3.8+
- pip

### Installation
```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install django djangorestframework django-cors-headers

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Start server
python manage.py runserver
```

Access admin panel at `http://localhost:8000/admin`

## Features

### Django Project Setup
- Complete Django 5.x REST API project
- Four functional apps: Blog, Events, Organizations, and Users
- Django REST Framework configured
- CORS headers configured for frontend integration
- SQLite database with complete schema

### Database Architecture
- Well-structured database models for all apps
- Complete migrations system
- Efficient data relationships
- Admin interface for data management

### Admin Panel
- Full-featured Django admin interface
- All models registered and accessible
- User-friendly data management
- Complete CRUD operations through admin

### Apps Overview

**Events App**: Campus events management system with event models including title, description, date, time, location, and categories.

**Organizations App**: Student organizations system with organization models, member management, and categorization.

**Users App**: User authentication and profile management with custom user models.

**Blog App**: Campus blog and news system for announcements and updates.

## Technologies Used
- Django 5.x
- Django REST Framework
- SQLite Database
- CORS Headers for API integration

## Contributors
**Wahid Sultani** - Full Stack Developer  
GitHub: [@Wahid123542](https://github.com/Wahid123542)


