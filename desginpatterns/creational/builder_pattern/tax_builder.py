from dataclasses import dataclass, field
from typing import List, Protocol


@dataclass
class Item:
    item_id: int = 0
    sku: str = ''
    name: str = ''
    price: float = 0.0
    weight: float = 0.0

    def __str__(self):
        return f'item_id={self.item_id}, price={self.price}, item_name={self.name}, item_weight={self.weight}'


@dataclass
class TaxRate:
    name: str = ''
    rate: float = 0.0


@dataclass
class Order:
    order_id: int = 0
    tracking_id: int = 0
    origination_id: str = 'orig-id'
    tags: List[str] = field(default_factory=[])
    items: List[Item] = field(default_factory=[])

    def __str__(self):
        return f'order_id= {self.order_id}, tracking_id= {self.tracking_id}, items={self.items}'


class IOrderBuilder(Protocol):
    def with_order_id(self, order_id: int) -> 'OrderBuilder':
        ...

    def with_origination_id(self, origination_id: str) -> 'OrderBuilder':
        ...

    def with_tracking_id(self, tracking_id: int) -> 'OrderBuilder':
        ...


class OrderBuilder(IOrderBuilder):

    def __init__(self):
        self.order_id = 0
        self.tracking_id = 0
        self.origination_id = 'origination_id'
        self.tags = []
        self.items = []

    def with_order_id(self, order_id: int) -> 'OrderBuilder':
        self.order_id = order_id
        return self

    def with_tracking_id(self, tracking_id: int) -> 'OrderBuilder':
        self.tracking_id = tracking_id
        return self

    def with_origination_id(self, origination_id: str) -> 'OrderBuilder':
        self.origination_id = origination_id
        return self

    def get_result(self):
        return Order(
            self.order_id,
            self.tracking_id,
            self.origination_id
        )


class Director:

    @classmethod
    def build(cls, order_builder: OrderBuilder):
        order_builder.with_order_id(124665) \
            .with_tracking_id(365324634) \
            .with_origination_id('Orig-order-124665')


# Client


print(Director.build(OrderBuilder()))