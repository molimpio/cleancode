from typing import Union

from src.domain.entity.order import Order
from src.domain.repository.order_repository import OrderRepository
from src.infra.database.connection import Connection


class OrderRepositoryPostgreSQL(OrderRepository):

    def __init__(self, connection: Connection):
        self.__connection = connection

    def get_by_code(self, code: str) -> Union[Order, None]:
        order_data = self.__connection.query('select cpf, issue_date, sequence from _order where code = %s', [code])
        if len(order_data) == 0:
            return None
        order_data = order_data[0]
        order = Order(cpf=order_data[0], issue_date=order_data[1], sequence=order_data[2])
        return order

    def save(self, order: Order) -> Union[Order, None]:
        params = [
            order.coupon, order.code.value, order.cpf.value, order.issue_date,
            order.freight.get_total(), order.sequence, order.get_total()
        ]
        sql = 'insert into _order (coupon, code, cpf, issue_date, freight, sequence, total) ' \
              'values (%s, %s, %s, %s, %s, %s, %s) returning id_order'

        order_id = self.__connection.insert(sql, params)

        if order_id > 0:
            return order
        else:
            return None

    def count(self) -> int:
        orders = self.__connection.query('select * from _order', [])
        return len(orders)
