import json
from pathlib import Path
import unittest
from src.pos_demo import total_order


class SampleConfigurationTests(unittest.TestCase):
    def test_changed_menu_and_order_integrate_with_configuration(self):
        root = Path(__file__).resolve().parents[1]
        config = json.loads((root / 'config/config.example.json').read_text())
        menu = {x['sku']: x for x in json.loads((root / 'data/menu_sample.json').read_text())}
        order = json.loads((root / 'data/order_sample.json').read_text())
        lines = [{'unit_price_cents': menu[x['sku']]['unit_price_cents'], 'quantity': x['quantity']} for x in order]
        self.assertEqual(total_order(lines, config['tax_basis_points']), {
            'subtotal_cents': 2225, 'tax_cents': 134, 'total_cents': 2359})
