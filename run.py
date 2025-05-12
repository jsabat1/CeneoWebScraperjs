from app import app

# Recommended Flask project structure for a more complex application:
#
# /CeneoWebScraperjs/
# ├── /app/                 # Application package
# │   ├── __init__.py       # Initialize the Flask app
# │   ├── routes.py         # Define application routes
# │   ├── models.py         # Define database models (if using a database)
# │   ├── forms.py          # Define forms (if using Flask-WTF)
# │   └── /templates/       # HTML templates
# │       └── index.html    # Example template
# │   └── /static/          # Static files (CSS, JS, images)
# │       ├── style.css     # Example CSS file
# │       └── script.js     # Example JS file
# ├── app.py                # Entry point for the application
# ├── config.py             # Configuration settings
# ├── requirements.txt      # Python dependencies
# ├── /migrations/          # Database migrations (if using Flask-Migrate)
# └── /venv/                # Virtual environment (optional, but recommended)
#
# Ensure your `index.html` file is placed in the `app/templates` folder.
