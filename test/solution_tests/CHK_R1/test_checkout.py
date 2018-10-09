import unittest

from solutions.CHK.checkout_solution import Product, Offer, Basket, checkout



class TestProduct(unittest.TestCase):

    def setUp(self):
        self.products = [
            {
                "sku": "A",
                "price": 50,
                "offer_id": 1
            },
            {
                "sku": "B",
                "price": 30,
                "offer_id": 2
            },
            {
                "sku": "C",
                "price": 20,
                "offer_id": None
            },
            {
                "sku": "D",
                "price": 15,
                "offer_id": None
            },
        ]

    def test_product_is_available(self):
        product = Product('A')
        self.assertTrue(product.is_available())

    def test_product_is_not_available(self):
        product = Product('X')
        self.assertFalse(product.is_available())

    def test_get_available_product_from_list(self):
        product = Product('a')
        self.assertEqual(1, len(product.get_product()))

    def test_get_not_available_product_from_list(self):
        product = Product('X')
        self.assertEqual(0, len(product.get_product()))

    def test_product_is_on_offer(self):
        product = Product('A')
        self.assertTrue(product.is_on_offer())

    def test_product_is_not_on_offer(self):
        product = Product('C')
        self.assertFalse(product.is_on_offer())

    def test_product_is_not_available_and_not_on_offer(self):
        product = Product('X')
        self.assertFalse(product.is_on_offer())


class TestOffer(unittest.TestCase):

    def setUp(self):
        self.offer = [
            {
                "offer_id": 1,
                "quantity": 3,
                "price": 130
            },
            {
                "offer_id": 2,
                "quantity": 2,
                "price": 45
            },
        ]

    def test_offer_is_available(self):
        offer = Offer(1)
        self.assertTrue(offer.is_available())

    def test_offer_is_not_available(self):
        offer = Offer(3)
        self.assertFalse(offer.is_available())

    def test_get_available_offer(self):
        offer = Offer(1)
        self.assertEqual(1, len(offer.get_offer()))

    def test_get_not_available_offer(self):
        offer = Offer(3)
        self.assertEqual(0, len(offer.get_offer()))


class TestBasket(unittest.TestCase):
    def setUp(self):
        self.valid_basket = u'A, b, C, D, E'
        self.not_valid_basket = u'%, B, 1'

    def test_is_valid_basket(self):
        basket = Basket(self.valid_basket)
        self.assertTrue(basket.is_valid())

    def test_is_not_valid_basket(self):
        basket = Basket(self.not_valid_basket)
        self.assertFalse(basket.is_valid())


class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.valid_basket = u'C, A, A, A, B, B'

    def test_checkout(self):
        self.assertEqual(195, checkout(self.valid_basket))


if __name__ == '__main__':
    unittest.main()
