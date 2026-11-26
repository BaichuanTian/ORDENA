"""A small checkout calculator for demonstrating controlled configuration changes."""
import json
from pathlib import Path


def total_order(lines, tax_basis_points):
    """Return integer-cent totals; round positive tax to nearest cent, half up."""
    if type(tax_basis_points) is not int or not 0 <= tax_basis_points <= 10000:
        raise ValueError('tax_basis_points must be an integer from 0 to 10000')
    if not isinstance(lines, list) or not lines:
        raise ValueError('order must contain at least one line')
    subtotal = 0
    for line in lines:
        if not isinstance(line, dict) or not {'unit_price_cents', 'quantity'} <= line.keys():
            raise ValueError('each order line must contain unit_price_cents and quantity')
        price, quantity = line['unit_price_cents'], line['quantity']
        if type(price) is not int or price < 0:
            raise ValueError('price must be a nonnegative integer number of cents')
        if type(quantity) is not int or not 1 <= quantity <= 99:
            raise ValueError('quantity must be an integer from 1 to 99')
        subtotal += price * quantity
    tax = (subtotal * tax_basis_points + 5000) // 10000
    return {'subtotal_cents': subtotal, 'tax_cents': tax, 'total_cents': subtotal + tax}


def run_demo():
    root = Path(__file__).resolve().parents[1]
    config = json.loads((root / 'config/config.example.json').read_text())
    menu = {item['sku']: item for item in json.loads((root / 'data/menu_sample.json').read_text())}
    order = json.loads((root / 'data/order_sample.json').read_text())
    lines = [{'unit_price_cents': menu[x['sku']]['unit_price_cents'], 'quantity': x['quantity']} for x in order]
    result = total_order(lines, config['tax_basis_points'])
    print(json.dumps({'restaurant': config['restaurant_name'], 'currency': config['currency'], **result}, indent=2))


if __name__ == '__main__':
    run_demo()
