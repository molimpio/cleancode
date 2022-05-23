from src.domain.repository.coupon_repository import CouponRepository
from src.domain.repository.item_repository import ItemRepository
from src.domain.repository.order_repository import OrderRepository
from src.domain.entity.order import Order
from src.application.usecase.place_order.place_order_input import PlaceOrderInput
from src.application.usecase.place_order.place_order_output import PlaceOrderOutput


class PlaceOrder:

    def __init__(self, item_repository: ItemRepository, order_repository: OrderRepository,
                 coupon_repository: CouponRepository):
        self.__item_repository = item_repository
        self.__order_repository = order_repository
        self.__coupon_repository = coupon_repository

    def execute(self, input_order: PlaceOrderInput) -> PlaceOrderOutput:
        sequence = self.__order_repository.count() + 1
        order = Order(input_order.cpf, input_order.date, sequence)

        for order_item in input_order.order_itens:
            item = self.__item_repository.get_by_id(order_item.get('id_item', None))

            if item is None:
                raise Exception('Item não encontrado')

            order.add_item(item, order_item.get('quantity'))

        if input_order.coupon:
            coupon = self.__coupon_repository.get_by_code(input_order.coupon)
            if coupon is not None:
                order.add_coupon(coupon)

        total = order.get_total()
        self.__order_repository.save(order)
        output = PlaceOrderOutput(total, order.code.value)
        return output
