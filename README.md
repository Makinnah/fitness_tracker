# Fitness Tracker API

An adaptive fitness tracking backend built with Django and Django REST Framework. Users can log, view, and analyze their fitness activities.

## Features
- User registration and authentication
- CRUD for fitness activities
- Activity history and metrics
- Optional goal setting and workout plans

## Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

#Setup Instructions
# Clone the repo
git clone https://github.com/Makinnah/fitness_tracker.git
cd fitness_tracker

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # Windows
# or
source venv/bin/activate      # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Start development server
python manage.py runserver
