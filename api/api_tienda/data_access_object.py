from api_tienda import db


class DataAccessObject:

    def __init__(self, entity_name=None):
        self.__db = db
        self.__entity_name = entity_name

    def _all_columns(self, columns):
        result = ""
        values = list(columns.values())
        for i in range(len(values)):
            if i == len(values) - 1:
                result += values[i]
            else:
                result += values[i] + ","
        return result

    def _sql_query(self, sql_query=""):
        cur = self.__db.get_cursor_no_dict()
        cur.execute(sql_query)
        return cur.fetchone()[0]

    def _get_all_as_dict(self, columns="*", condition=""):
        cur = self.__db.get_cursor()
        cur.execute(f"SELECT {columns} FROM {self.__entity_name} {condition};")
        return cur.fetchall()

    def _get_one_as_dict(self, columns="*", condition=""):
        cur = self.__db.get_cursor()
        cur.execute(f"SELECT {columns} FROM {self.__entity_name} {condition};")
        return cur.fetchone()

    def _update(self, sql_params=""):
        cur = self.__db.get_cursor()
        cur.execute(f"UPDATE {self.__entity_name} SET {sql_params};")
        cur.connection.commit()

    def _delete(self, condition=""):
        cur = self.__db.get_cursor()
        cur.execute(f"DELETE FROM {self.__entity_name} {condition};")
        cur.connection.commit()

    def _save(self, sql_params=""):
        cur = self.__db.get_cursor()
        cur.execute(f'''INSERT INTO {self.__entity_name} VALUES({sql_params});''')
        cur.connection.commit()





