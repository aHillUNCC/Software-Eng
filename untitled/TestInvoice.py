import pytest
from Invoice import Invoice

@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanCalculateTotalImpurePrice(invoice, products):
    invoice.totalImpurePrice(products)
    assert invoice.totalIMpurePrice(products) == 75

def test_CanCalculateTotalDiscount(invoice, products):
    invoice.totalDiscount(products)
    assert invoice.totalIMpurePrice(products) == 5.62

def test_CanCalculateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalIMpurePrice(products) == 69.38