#application.py
from os import environ
from FlaskWebProject import app



# WSGI callable for Azure / Gunicorn
application = app

if __name__ == '__main__':
    host = environ.get('SERVER_HOST', '0.0.0.0')
    port = int(environ.get('SERVER_PORT', 8000))
    application.run(host=host, port=port, debug=True)  

from flask_login import LoginManager
from models import User  # your User model

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # adjust depending on your DB
