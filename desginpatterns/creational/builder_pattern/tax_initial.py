class Rate:
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate


class Order:
    def __init__(self, order_id, tracking_id, origination_id, items):
        self.order_id = order_id
        self.tracking_id = tracking_id
        self.origination_id = origination_id
        self.items = items


class Item:
    def __init__(self, item_id, sku, name, weight, price):
        self.item_id = item_id
        self.sku = sku
        self.name = name
        self.weight = weight
        self.price = price


class TaxCalculator:
    @staticmethod
    def calculate(order: Order, rate: Rate):
        return order.items.price * rate.rate


# Client
item = Item(111, 3356324, 'Television', 11, 100)
wa_rate = Rate('WA State Sales Tax', 10.1)
order1 = Order(81352, 119463, 'wa-stax-111', item)


tax = TaxCalculator.calculate(order1, wa_rate)
assert tax == 999, f"{tax}"

"""
    How many issues in this simple test:
    - Despite of the simplicity of the test, the test requires the reader to parse a huge amount of code to get 
    the correct state of the test.
    - Where does the 1010.0 come from? How we know which attribute needed to calculate the tax? 
"""


