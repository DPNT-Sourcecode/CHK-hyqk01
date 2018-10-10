import itertools


class Product(object):
    products_list = [
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

    def __init__(self, sku):
        self.sku = sku

    def is_available(self):
        if any(product.get('sku') == self.sku for product in self.products_list):
            return True
        return False

    def get_product(self):
        if self.is_available():
            for idx, product in enumerate(self.products_list):
                if self.sku == product.get('sku'):
                    return [self.products_list[idx]]
        return []

    def is_on_offer(self):
        if self.is_available() and self.get_product()[0]['offer_id'] is not None:
            return True
        return False


class Offer(object):
    offers_list = [
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
                "price": None,
                "sku": "B",
                "sku_quantity": 1
            },
        ]

    def __init__(self, id):
        self.id = id

    def is_available(self):
        if any(offer.get('offer_id') == self.id for offer in self.offers_list):
            return True
        return False

    def get_offer(self):
        if self.is_available():
            for idx, offer in enumerate(self.offers_list):
                if self.id == offer.get('offer_id'):
                    return [self.offers_list[idx]]
        return []


class Basket(object):
    def __init__(self, skus, products=None):
        self.skus = [sku for sku in skus]
        self.products = products if products else []

    def is_valid(self):
        if all(sku.isalpha() for sku in self.skus) or not self.skus:
            return True
        return False


def checkout(skus):
    basket = Basket(skus)
    if not basket.is_valid():
        return -1

    prod_sku = ''.join(sorted(skus))
    for sku in prod_sku:
        if Product(sku).is_available():
            basket.products.append(Product(sku))
        else:
            return -1

    offer_applied = False
    offers = [Offer(product.get_product()[0].get('offer_id')) for product in basket.products]
    for offer in offers:
        if offer.get_offer() and not offer_applied:
            price = offer.get_offer()[0].get('price')
            if not price:
                product_for_free = offer.get_offer()[0].get('sku')
                product_for_free_quantity = offer.get_offer()[0].get('sku_quantity')
                prod_sku = prod_sku.replace(product_for_free, '', product_for_free_quantity)

                basket.products = []
                for sku in prod_sku:
                    if Product(sku).is_available():
                        basket.products.append(Product(sku))
                    else:
                        return -1
                offer_applied = True

    product_groups = []
    for sku, group in itertools.groupby(basket.products, key=lambda x: x.get_product()[0].get('sku')):
        product_groups.append((sku, len(list(group))))

    total = 0
    for group in product_groups:
        product = Product(group[0])

        product_price = product.get_product()[0].get('price')
        if product.is_on_offer():
            offer = Offer(product.get_product()[0].get('offer_id'))
            offer_price = offer.get_offer()[0].get('price')
            if offer_price:
                offer_quantity = offer.get_offer()[0].get('quantity')

                quo, rem = divmod(group[1], offer_quantity)
                total += quo * offer_price + rem * product_price
            else:
                total += group[1] * product_price
        else:
            total += group[1] * product_price

    return total
