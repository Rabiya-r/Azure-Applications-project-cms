import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # Flask Secret Key
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")

    # Azure Blob Storage
    BLOB_ACCOUNT = os.environ.get("BLOB_ACCOUNT", "cmsblobacc")
    BLOB_STORAGE_KEY = os.environ.get("BLOB_STORAGE_KEY", "i5x4gM9LvuL9iR8I3W+0PVzTBms5LZGOYsy0JO876jlxyt1WdbZWUTz4v4xxhAhaYagDNjtH/nSO+ASt8YkPFg==")
    BLOB_CONTAINER = os.environ.get("BLOB_CONTAINER", "images")

    # Azure SQL Database
    SQL_SERVER = os.environ.get("SQL_SERVER", "cmssqlserver.database.windows.net")
    SQL_DATABASE = os.environ.get("SQL_DATABASE", "cmssqldb")
    SQL_USER_NAME = os.environ.get("SQL_USER_NAME", "sqladmin")
    SQL_PASSWORD = os.environ.get("SQL_PASSWORD", "912002@Rabiya")

    # ✅ Corrected connection string format
    SQLALCHEMY_DATABASE_URI = (
        f"mssql+pyodbc://{SQL_USER_NAME}:{SQL_PASSWORD}@{SQL_SERVER}:1433/"
        f"{SQL_DATABASE}?driver=ODBC+Driver+17+for+SQL+Server"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft Authentication
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET", "W1.8Q~.kTj8x5A6p2_JpJpZKn2PYE9Yz8x614bnL")
    CLIENT_ID = os.environ.get("CLIENT_ID", "c9f1657f-cfb9-4aad-862c-355390aba654")
    AUTHORITY = "https://login.microsoftonline.com/common"
    REDIRECT_PATH = "/getAToken"
    SCOPE = ["User.Read"]
    SESSION_TYPE = "filesystem"
