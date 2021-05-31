import os
from flask import Config
import urllib.parse as urlparse


class BDConfig(Config):
    MYSQL_HOST = "localhost"
    MYSQL_USER = "root"
    MYSQL_PASSWORD = ""
    MYSQL_DB = "tienda"

