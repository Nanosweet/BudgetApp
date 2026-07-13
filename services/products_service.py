class ProductsService:
    def __init__(self, products):
        self.products = products
    def get_available_products(self):
        return [
            f"{product['nazwa']} {product['cena']}"
            for product in self.products
            if product['dostepny'] == 'tak'
        ]