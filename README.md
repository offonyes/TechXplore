# Tutor Application

## Description
This project is a web application for searching and booking tutors. Users can register as students or tutors, leave reviews and view tutor ratings.

## Functionality
- Registration of users with choice of role (student or tutor)
- Uploading photos of tutors
- Rating Tutor from students(In Future)
- View tutor ratings 
- Getting a list of available cities for tutors

## Requirements
- Python 3.12+
- Django 5.0+
- SQLite3

## API Endpoints
The core functionality is accessible via REST API endpoints. To view the detailed API documentation, see the swagger documentation at
```python
http://127.0.0.1:8000/api/schema/swagger-ui/
```
## Installation
- Python 3.12
1. Clone the repository:
```shell
git clone https://github.com/offonyes/TechXplore
```
2. Install dependencies:
```shell
pip install -r requirements.txt
```
3. Apply migrations:
```shell
py manage.py migrate
```
4. Create SuperUser:
```shell
py manage.py createsuperuser
```
6. Run the development server:

```shell
py manage.py runserver
```

## Usage
- Navigate to the admin interface to manage tutor.
- Navigate to '/api/schema/swagger-ui/' to see swagger.
