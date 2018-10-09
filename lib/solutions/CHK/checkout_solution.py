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

    def is_available(self):
        pass


class Offer(object):
    pass


def checkout(skus):
    raise NotImplementedError()
