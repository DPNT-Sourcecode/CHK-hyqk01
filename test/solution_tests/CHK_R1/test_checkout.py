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
            {
                "sku": "E",
                "price": 40,
                "offer_id": 3
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
        self.assertEqual(0, len(product.get_product()))

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
                "price": 130,
            },
            {
                "offer_id": 2,
                "quantity": 2,
                "price": 45
            },
            {
                "offer_id": 3,
                "quantity": 2,
                "price": 0,
                "sku": "B",
                "sku_quantity": 1
            }
        ]

    def test_offer_is_available(self):
        offer = Offer(1)
        self.assertTrue(offer.is_available())

    def test_offer_is_not_available(self):
        offer = Offer(100)
        self.assertFalse(offer.is_available())

    def test_get_available_offer(self):
        offer = Offer(1)
        self.assertEqual(1, len(offer.get_offer()))

    def test_get_not_available_offer(self):
        offer = Offer(100)
        self.assertEqual(0, len(offer.get_offer()))


class TestBasket(unittest.TestCase):
    def setUp(self):
        self.valid_basket_1 = u'AbCDE'
        self.valid_basket_2 = u''
        self.not_valid_basket = u'%B1'

    def test_is_valid_basket(self):
        basket_1 = Basket(self.valid_basket_1)
        self.assertTrue(basket_1.is_valid())

        basket_2 = Basket(self.valid_basket_2)
        self.assertTrue(basket_2.is_valid())

    def test_is_not_valid_basket(self):
        basket = Basket(self.not_valid_basket)
        self.assertFalse(basket.is_valid())


class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.valid_basket_1 = u'CAAABB'
        self.valid_basket_2 = u'BABC'
        self.valid_basket_3 = u''
        self.valid_basket_4 = u'EEB'
        self.valid_basket_5 = u'EEBB'
        self.valid_basket_6 = u'E'
        self.valid_basket_7 = u'ABCDE'
        self.valid_basket_8 = u'EEEEBB'
        self.valid_basket_9 = u'ABCDEABCDE'

    def test_checkout(self):
        self.assertEqual(195, checkout(self.valid_basket_1))
        self.assertEqual(115, checkout(self.valid_basket_2))
        self.assertEqual(0, checkout(self.valid_basket_3))
        self.assertEqual(80, checkout(self.valid_basket_4))
        self.assertEqual(110, checkout(self.valid_basket_5))
        self.assertEqual(40, checkout(self.valid_basket_6))
        self.assertEqual(155, checkout(self.valid_basket_7))
        self.assertEqual(160, checkout(self.valid_basket_8))
        self.assertEqual(280, checkout(self.valid_basket_9))


if __name__ == '__main__':
    unittest.main()
