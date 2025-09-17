"""
This script exposes the FlaskWebProject application as a WSGI callable.
Azure App Service / Gunicorn will use this file to run the app.
"""

from FlaskWebProject import app  # import your Flask app

# Rename app object to 'application' for Azure
application = app

# Optional: only run dev server if executed directly (not used by Gunicorn)
if __name__ == '__main__':
    from os import environ
    host = environ.get('SERVER_HOST', '0.0.0.0')  # Azure binds to 0.0.0.0
    try:
        port = int(environ.get('SERVER_PORT', '8000'))
    except ValueError:
        port = 8000
    # Remove ssl_context for dev in Azure or keep for local testing
    application.run(host, port, debug=True, ssl_context='adhoc')
