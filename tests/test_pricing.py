from shop.cart import Cart
from shop.pricing import percent_of, total


def test_total_is_items_plus_vat_plus_shipping():
    cart = Cart(shipping=500).add("a", 10000)
    assert total(cart) == 10000 + 2200 + 500


def test_shipping_is_not_taxed():
    assert total(Cart(shipping=700)) == 700


def test_percent_of_rounds_down():
    assert percent_of(1999, 15) == 299
