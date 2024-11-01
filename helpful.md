mycv/                     # Root directory of your project
    manage.py             # Manage script for Django
    mycv/                 # Project directory (same name as your project)
        __init__.py
        settings.py       # Settings for your project
        urls.py           # Project-level URL configurations
        wsgi.py
    portfolio/            # Your app directory
        migrations/       # Directory for migration files
        templates/        # Directory for HTML templates
            portfolio/    # Subdirectory for your app's templates
                home.html
                projects.html
        __init__.py
        models.py         # Model definitions
        views.py          # View functions
        urls.py           # App-level URL configurations

