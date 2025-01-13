Project Management system
----------------------------
- Django Project with Project, Task, and Team Management APIs


## Features
- User Authentication with simpleJWT.
- CRUD API for Projects(APIView), Tasks, and Team Management(Viewset).
- Validations and Error Handling.
- API Documentation with Swagger in Project CRUID

## Requirements
- Python 3.9 or higher
- Django 5.1.4
- Django REST Framework
- djangorestframework_simplejwt
- drf-yasg (for Swagger API documentation)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>

2. Create and activate a virtual environment:
python3 -m venv env
source venv/bin/activate 

3. Create Project:
django-admin startproject project_name .

4. Create apps:
python3 manage.py startapp app_name

5. Install dependencies:
pip install -r requirements.txt

6. Apply migrations:
python3 manage.py makemigrations
python3 manage.py migrate

7. Run the development server:
python manage.py runserver

8. Access the API documentation at:
http://127.0.0.1:8000/swagger/


