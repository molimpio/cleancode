import unittest
from src.infra.database.postgre_sql_connection_adapter import PostgreSQLConnectionAdapter
from src.infra.repository.postgresql.item_repository_postgresql import ItemRepositoryPostgreSQL


class ItemRepositoryPostgreSQLTestCase(unittest.TestCase):
    def test_repositorio_buscando_um_item(self):
        connection = PostgreSQLConnectionAdapter()
        item_repository = ItemRepositoryPostgreSQL(connection)
        item = item_repository.get_by_id(1)
        self.assertEqual('Guitarra', item.description)
        connection.close()


if __name__ == '__main__':
    unittest.main()
