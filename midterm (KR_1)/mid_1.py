from typing import Self
import unittest

class ShoppingCart:
    def __init__(self):
        self.__items = {}

    def add_item(self, name: str, price: float, quantity: int = 1) -> Self:
        if price <= 0 or quantity <= 0:
            raise ValueError('Price and quantity must be greater than zero.')

        if name in self.__items:
            current_items = self.__items[name]
            found = False
            for existing_item in current_items:
                existing_price, existing_quantity = existing_item
                if existing_price == price:
                    existing_item[1] += quantity
                    found = True
                    break
            if not found:
                current_items.append([price, quantity])
        else:
            self.__items[name] = [[price, quantity]]

        return self

    def __len__(self) -> int:
        return len(self.__items)

    @property
    def total_cost(self) -> float:
        total = 0
        for item_list in self.__items.values():
            for price, quantity in item_list:
                total += price * quantity
        return total

    def __str__(self) -> str:
        result = 'Shopping Cart:\n'
        for name, item_list in self.__items.items():
            for price, quantity in item_list:
                result += f'{name}: {quantity} at ${price:.2f} each\n'
        result += f'Total cost: ${self.total_cost:.2f}'
        return result


cart = ShoppingCart()
cart.add_item('Apple', 0.5, 3)
cart.add_item('Banana', 0.3, 5)
cart.add_item('Apple', 0.5, 2)
cart.add_item('Apple', 0.1, 3)
# You may implement fluent interface as well:
# cart.add_item('Apple', 0.5, 3).add_item('Banana', 0.3, 5).add_item('Apple', 0.5, 2)
print(cart)  # Should display the items and total cost
print(f'Total items: {len(cart)}')  # Should display total unique items in the cart

"""
For validation unittests
with self.assertRaises(ValueError):
    cart.add_item('Banana', 0.1, -2)
"""

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_item(self):
        self.cart.add_item('Orange', 0.8, 4)
        self.cart.add_item('Orange', 0.8, 2)
        self.cart.add_item('Orange', 0.5, 3)
        self.cart.add_item('Strawberry', 1.3, 9)
        self.assertEqual(str(self.cart),'Shopping Cart:\nOrange: 6 at $0.80 each\nOrange: 3 at $0.50 each\nStrawberry: 9 at $1.30 each\nTotal cost: $18.00')

    def test_len(self):
        self.cart.add_item('Watermelon', 3.0, 2)
        self.cart.add_item('Watermelon', 6.0, 3)
        self.cart.add_item('Mango', 2.5, 8)
        self.cart.add_item('Pumpkin', 0.4, 1)
        self.assertEqual(len(self.cart), 3)

    def test_total_cost(self):
        self.cart.add_item('Lemon', 5.0, 2)
        self.cart.add_item('Grapefruit', 9.0, 3)
        self.cart.add_item('Potato', 2.5, 4)
        self.assertEqual(self.cart.total_cost, 47)

    def test_raise_value_error(self):
        with self.assertRaises(ValueError):
            cart.add_item('Banana', 0.1, -2)
        with self.assertRaises(ValueError):
            cart.add_item('Banana', -0.1, 2)
        with self.assertRaises(ValueError):
            cart.add_item('Cucumber', 0, 3)
        with self.assertRaises(ValueError):
            cart.add_item('Tomato', 0.6, 0)

if __name__ == '__main__':
    unittest.main()