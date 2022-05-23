from src.domain.entity.freight import Freight
from src.domain.repository.item_repository import ItemRepository
from .simulate_freight_input import SimulateFreightInput
from .simulate_freight_output import SimulateFreightOutput


class SimulateFreight:

    def __init__(self, item_repository: ItemRepository):
        self.__item_repository = item_repository

    def execute(self, input_simulate: SimulateFreightInput) -> SimulateFreightOutput:
        freight = Freight()
        for order_item in input_simulate.order_itens:
            item = self.__item_repository.get_by_id(order_item.get('id_item', None))

            if item is None:
                raise Exception('Item não encontrado')

            freight.add_item(item, order_item.get('quantity'))

        output = SimulateFreightOutput(freight.get_total())
        return output
