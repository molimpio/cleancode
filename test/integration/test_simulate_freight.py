import unittest
from src.infra.repository.memory.item_repository_memory import ItemRepositoryMemory
from src.application.usecase.simulate_freight.simulate_freight import SimulateFreight
from src.application.usecase.simulate_freight.simulate_freight_input import SimulateFreightInput


class SimulateFreightTest(unittest.TestCase):
    def test_deve_simular_frete_pedido(self):
        item_repository = ItemRepositoryMemory()
        simulate_freight = SimulateFreight(item_repository)
        order_itens = [
            {'id_item': 1, 'quantity': 1},
            {'id_item': 2, 'quantity': 1},
            {'id_item': 3, 'quantity': 3},
        ]
        simulate_freight_input = SimulateFreightInput(order_itens)
        output = simulate_freight.execute(simulate_freight_input)
        self.assertEqual(output.total, 260)


if __name__ == '__main__':
    unittest.main()
