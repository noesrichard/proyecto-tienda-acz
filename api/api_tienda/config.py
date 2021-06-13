import os
from flask import Config
import urllib.parse as urlparse


class BDConfig(Config):
    MYSQL_HOST = "localhost"
    MYSQL_USER = "rmcv"
    MYSQL_PASSWORD = ""
    MYSQL_PORT= 3308
    MYSQL_DB = "tienda"


if 'CLEARDB_DATABASE_URL' in os.environ:
    class ClearDBConfig(Config):
        urlparse.uses_netloc.append('mysql')
        url = urlparse.urlparse(os.environ['CLEARDB_DATABASE_URL'])
        MYSQL_DB = url.path[1:]
        MYSQL_USER = url.username
        MYSQL_PASSWORD = url.password
        MYSQL_HOST = url.hostname
        MYSQL_PORT = url.port
