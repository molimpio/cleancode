import unittest
from src.infra.database.postgre_sql_connection_adapter import PostgreSQLConnectionAdapter


class ConnectionTest(unittest.TestCase):
    def test_conexao_com_banco_dados_postgres(self):
        connection = PostgreSQLConnectionAdapter()
        items = connection.query('select * from item', [])
        self.assertTrue(len(items) > 0)
        connection.close()


if __name__ == '__main__':
    unittest.main()
