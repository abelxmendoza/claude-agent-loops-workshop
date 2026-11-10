from shop.cart import Cart
from shop.receipt import money, render


def test_money_always_shows_two_decimals():
    assert money(2450) == "24.50 EUR"
    assert money(780) == "7.80 EUR"
    assert money(0) == "0.00 EUR"


def test_render_amounts_all_have_two_decimals():
    cart = Cart(shipping=590).add("Espresso beans 1kg", 2450).add("Filter papers", 390, qty=2)
    for line in render(cart).splitlines():
        amount = line.rsplit(" ", 2)[-2]
        assert len(amount.split(".")[-1]) == 2
