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
3. Navigate to the root ./ directory of the product and run `env\Scripts\Activate` to start a virtual Python environment
4. Run `pip install -r requirements.txt` to install our local dependencies
5. Run `python manage.py makemigrations` and `python manage.py migrate` to initialize your local database
5. Run `python manage.py runserver` to serve this application over `localhost`