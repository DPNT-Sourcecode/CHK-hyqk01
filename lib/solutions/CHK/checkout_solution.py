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
        ]

    def __init__(self, sku):
        self.sku = sku.upper()

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
                "price": 130
            },
            {
                "offer_id": 2,
                "quantity": 2,
                "price": 45
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
        self.skus = skus.replace(' ', '').split(',')
        self.products = products if products else []

    def is_valid(self):
        if all(sku.isalpha() for sku in self.skus):
            return True
        return False


def checkout(skus):
    basket = Basket(skus)
    if not basket.is_valid():
        return -1

    skus = skus.replace(' ', '').split(',')
    skus.sort()

    for sku in skus:
        if Product(sku).is_available():
            basket.products.append(Product(sku))
        else:
            return -1

    product_groups = []
    for sku, group in itertools.groupby(basket.products, key=lambda x: x.get_product()[0].get('sku')):
        product_groups.append((sku, len(list(group))))

    total = 0
    for group in product_groups:
        product = Product(group[0])

        product_price = product.get_product()[0].get('price')
        # import ipdb; ipdb.set_trace()
        if product.is_on_offer():
            offer = Offer(product.get_product()[0].get('offer_id'))
            offer_price = offer.get_offer()[0].get('price')
            offer_quantity = offer.get_offer()[0].get('quantity')

            quo, rem = divmod(group[1], offer_quantity)
            total += quo * offer_price + rem * product_price
        else:
            total += group[1] * product_price

    return total
