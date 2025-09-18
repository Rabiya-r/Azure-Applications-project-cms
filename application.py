from os import environ
from FlaskWebProject import app

# WSGI callable for Azure / Gunicorn
application = app

# Optional: only run Flask dev server locally
if __name__ == '__main__':
    host = environ.get('SERVER_HOST', '0.0.0.0')
    port = int(environ.get('SERVER_PORT', 8000))
    application.run(host=host, port=port, debug=True)  
