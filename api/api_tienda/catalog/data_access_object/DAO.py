

from api_tienda import db


class DAO:

    def __init__(self, entity_name=None):
        self.__db = db
        self.__entity_name = entity_name

    def get_all(self):
        cur = self.__db.get_cursor()
        cur.execute(f"SELECT * FROM {self.__entity_name};")
        return cur.fetchall()

    def _save(self, sql_params):
        cur = self.__db.get_cursor()
        cur.execute(f'''INSERT INTO {self.__entity_name} 
                VALUES({sql_params});''')
        cur.connection.commit()

    def _get_all_by(self, condition):
        cur = self.__db.get_cursor()
        cur.execute(f"SELECT * FROM {self.__entity_name} {condition};")
        return cur.fetchall()

    def _get_one_by(self, condition):
        cur = self.__db.get_cursor()
        cur.execute(f"SELECT * FROM {self.__entity_name} {condition};")
        return cur.fetchone()

    def _update(self, sql_params=""):
        cur = self.__db.get_cursor()
        cur.execute(f"UPDATE {self.__entity_name} SET {sql_params};")
        cur.connection.commit()

    def _delete(self, condition=""):
        cur = self.__db.get_cursor()
        cur.execute(f"DELETE FROM {self.__entity_name} {condition};")
        cur.connection.commit()