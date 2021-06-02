from flask_mysqldb import MySQL
import MySQLdb


class DBConnection(MySQL):

    def __init__(self, app):
        self.__msyql = MySQL(app)

    def get_connection(self):
        return self.__msyql

    def get_cursor(self):
        return self.__msyql.connection.cursor(MySQLdb.cursors.DictCursor)

    def get_cursor_no_dict(self):
        return self.__msyql.connection.cursor()