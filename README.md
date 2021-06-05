# Starter Django project 3.2.3

Starting redesign of jnuttedev.com website. Project is built with Django, Sass, and some Bulma. Blog posts now converts markdown to HTML, saves timestamp for added/updated posts.

### To generate sass files 

Using [django-sass](https://github.com/coderedcorp/django-sass)

The following will watch for new updates in your sass files, but must be run alongside the server

`./manage.py sass static/sass/ static/css/ --watch`

Run the server and watch for new sass file changes:

`./manage.py sass static/sass/ static/css/ --watch & ./manage.py runserver`

### Generate a new secret key

`python generate_secret.py`
