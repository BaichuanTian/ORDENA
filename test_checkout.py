import unittest
from src.pos_demo import total_order


class CheckoutTests(unittest.TestCase):
    def test_normal_order(self):
        result = total_order([{'unit_price_cents': 750, 'quantity': 2}, {'unit_price_cents': 325, 'quantity': 1}], 600)
        self.assertEqual(result, {'subtotal_cents': 1825, 'tax_cents': 110, 'total_cents': 1935})

    def test_half_cent_rounds_up(self):
        self.assertEqual(total_order([{'unit_price_cents': 5, 'quantity': 1}], 1000)['tax_cents'], 1)

    def test_zero_tax(self):
        self.assertEqual(total_order([{'unit_price_cents': 100, 'quantity': 1}], 0)['total_cents'], 100)

    def test_quantity_boundaries(self):
        for quantity in [1, 99]:
            with self.subTest(quantity=quantity):
                self.assertEqual(total_order([{'unit_price_cents': 100, 'quantity': quantity}], 0)['total_cents'], 100 * quantity)

    def test_invalid_quantity(self):
        for quantity in [0, -1, 100, 1.5, True]:
            with self.subTest(quantity=quantity), self.assertRaises(ValueError):
                total_order([{'unit_price_cents': 100, 'quantity': quantity}], 600)

    def test_invalid_price(self):
        for price in [-1, 1.5, True]:
            with self.subTest(price=price), self.assertRaises(ValueError):
                total_order([{'unit_price_cents': price, 'quantity': 1}], 600)

    def test_empty_order(self):
        with self.assertRaises(ValueError):
            total_order([], 600)

    def test_invalid_tax(self):
        for tax in [-1, 10001, 6.5, True]:
            with self.subTest(tax=tax), self.assertRaises(ValueError):
                total_order([{'unit_price_cents': 100, 'quantity': 1}], tax)


if __name__ == '__main__':
    unittest.main()
