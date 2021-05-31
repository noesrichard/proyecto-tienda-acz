import os
from flask import Config
import urllib.parse as urlparse


class BDConfig(Config):
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "tienda"

class ClearDBConfig(Config):
    urlparse.uses_netloc.append('mysql')
    url = urlparse.urlparse(os.environ['CLEARDB_DATABASE_URL'])
    MYSQL_DB = url.path[1:]
    MYSQL_USER = url.username
    MYSQL_PASSWORD = url.password
    MYSQL_HOST = url.hostname
    MYSQL_PORT = url.port