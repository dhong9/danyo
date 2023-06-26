# [Danyo](https://dhong9.pythonanywhere.com/)[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/danielhong35/)

![Django CI](https://github.com/dhong9/danyo/actions/workflows/django.yml/badge.svg)

This is the API that my [portfolio website](https://www.danyo.tech) interfaces with. It is developed with Django and hosted on [Python Anywhere](https://pythonanywhere.com/).

_Automated Build and Deployment_
All components are automatically tested with [Github's pipeline](https://github.com/dhong9/danyo/actions). Code coverage results are posted to [CodeCov](https://app.codecov.io/gh/dhong9/danyo).

**HELPFUL LINKS**

- View [Github Repository](https://github.com/dhong9/danyo)
- Check [API Home Page](https://dhong9.pythonanywhere.com/)
- See [Code Coverage](https://app.codecov.io/gh/dhong9/danyo)

#### Resources

This API was built with the following resources:

- [Django](https://www.djangoproject.com/) - Framework that the API is built on
- [Codecov](https://about.codecov.io/) - Measures unit test coverage

## Quick Start

Quick start options:

- Clone or Fork from [Github](https://github.com/dhong9/danyo)

## Terminal Commands

1. Download and Install Python 3.11 version from [Python Official Page](https://www.python.org/downloads/)
2. In `settings.py`, add `"localhost"` to CORS Whitelist and Allowed Host list
3. Make a `.env` file to define `SECRET_KEY` and `EMAIL_PASSWORD` 
4. Navigate to the root ./ directory of the product and run `env\Scripts\Activate` to start a virtual Python environment
5. Run `pip install -r requirements.txt` to install our local dependencies
6. Run `python manage.py makemigrations` and `python manage.py migrate` to initialize your local database
7. Run `python manage.py runserver` to serve this application over `localhost`

### What's Included

Within the download, you'll find the following directories and files:

```
danyo
    ├── .github
    │   ├── workflows
    |   │   ├── django.yml
    ├── portfolio
    │   ├── accounts
    |   │   ├── migrations
    |   |   │   ├── __init__.py
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── models.py
    │   │   ├── serializer.py
    │   │   ├── tests.py
    │   │   ├── urls.py
    │   │   ├── views.py
    │   ├── threadly
    │   │   ├── __init__.py
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── models.py
    │   │   ├── serializer.py
    │   │   ├── tests.py
    │   │   ├── views.py
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    ├── manage.py
    ├── README.py
    ├── requirements.txt
```