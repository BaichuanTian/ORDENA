import unittest
from src.pos_demo import total_order


class LineValidationTests(unittest.TestCase):
    def test_missing_required_keys(self):
        for line in [{}, {'unit_price_cents': 100}, {'quantity': 1}]:
            with self.subTest(line=line), self.assertRaises(ValueError):
                total_order([line], 600)

    def test_non_dictionary_lines(self):
        for line in [None, 100, 'item', []]:
            with self.subTest(line=line), self.assertRaises(ValueError):
                total_order([line], 600)

    def test_valid_dictionary_allows_extra_metadata(self):
        self.assertEqual(
            total_order([{'unit_price_cents': 100, 'quantity': 2, 'sku': 'TEA'}], 600),
            {'subtotal_cents': 200, 'tax_cents': 12, 'total_cents': 212})

    def test_later_malformed_line_prevents_result(self):
        with self.assertRaises(ValueError):
            total_order([{'unit_price_cents': 100, 'quantity': 1}, {}], 600)
