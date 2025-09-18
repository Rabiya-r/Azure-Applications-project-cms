from datetime import datetime
from FlaskWebProject import db
from werkzeug.utils import secure_filename
from flask import flash, current_app
from azure.storage.blob import BlobServiceClient
import string, random

def id_generator(size=32, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"<User {self.username}>"

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(75), nullable=False)
    body = db.Column(db.String(800), nullable=False)
    image_path = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f"<Post {self.title}>"

    def save_changes(self, form, file, userId, new=False):
        """Save or update post with optional blob image upload"""
        self.title = form.title.data
        self.author = form.author.data
        self.body = form.body.data
        self.user_id = userId

        if file:
            filename = secure_filename(file.filename)
            ext = filename.rsplit('.', 1)[-1].lower()
            new_filename = id_generator(16) + "." + ext

            try:
                # Setup blob client dynamically
                storage_url = f"https://{current_app.config['BLOB_ACCOUNT']}.blob.core.windows.net/"
                blob_service = BlobServiceClient(
                    account_url=storage_url,
                    credential=current_app.config['BLOB_STORAGE_KEY']
                )
                blob_client = blob_service.get_blob_client(
                    container=current_app.config['BLOB_CONTAINER'],
                    blob=new_filename
                )
                blob_client.upload_blob(file, overwrite=True)

                # Delete old blob if replacing
                if self.image_path:
                    old_blob = blob_service.get_blob_client(
                        container=current_app.config['BLOB_CONTAINER'],
                        blob=self.image_path
                    )
                    try:
                        old_blob.delete_blob()
                    except Exception:
                        pass

                self.image_path = new_filename
            except Exception as e:
                flash(f"Image upload failed: {e}", "danger")

        if new:
            db.session.add(self)
        db.session.commit()
