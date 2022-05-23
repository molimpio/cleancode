import psycopg2
from src.infra.database.connection import Connection


class PostgreSQLConnectionAdapter(Connection):

    def __init__(self):
        self.__connection = psycopg2.connect(dbname='cleancode', user='postgres', password='1234', host='localhost')

    def query(self, sql: str, params: list) -> list:
        cursor = self.__connection.cursor()
        cursor.execute(sql, params)
        results = cursor.fetchall()
        return results

    def insert(self, sql: str, params: list) -> int:
        cursor = self.__connection.cursor()
        cursor.execute(sql, params)
        self.__connection.commit()
        register_inserted = cursor.fetchone()
        return register_inserted[0]

    def close(self) -> None:
        self.__connection.close()
