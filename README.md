# Starter Django project 3.2.3

Redesign of jnuttedev.com website. Project is built with Django, Sass, and some Bulma. Uses Wagtail on the backend to manage content. Blog posts now converts markdown to HTML, saves timestamp for added/updated posts.

Project uses [Poetry](https://github.com/python-poetry/poetry) for dependency management.

`poetry shell`

`poetry install`

`./manage runserver`


### To generate sass files in development

Using [django-sass](https://github.com/coderedcorp/django-sass)

The following will watch for new updates in your sass files, but must be run alongside the server

`./manage.py sass static/sass/ static/css/ --watch`

Run the server and watch for new sass file changes:

`./manage.py sass static/sass/ static/css/ --watch & ./manage.py runserver`

### Generate a new secret key

`python generate_secret.py`

### To login to wagtail

`127.0.0.1:8000/cms`

# Use Tailwind in development

`./manage.py tailwind start`