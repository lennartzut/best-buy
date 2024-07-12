class Store:
    def __init__(self, product_list):
        self.product_list = product_list

    def add_product(self, product):
        """Add product to the store."""
        self.product_list.append(product)

    def remove_product(self, product):
        """Remove product from store"""
        if product in self.product_list:
            self.product_list.remove(product)

    def get_total_quantity(self):
        """Return how many items are in the store in total."""
        total_quantity = 0
        for product in self.product_list:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """Return all products in the store that are active."""
        all_active_products = []
        for product in self.product_list:
            if product.is_active():
                all_active_products.append(product)
        return all_active_products

    def order(self, shopping_list):
        """Get a list of tuples. Buy the products and return the
        total price of the order"""
        total_price = 0.0
        for product, quantity in shopping_list:
            if not product.is_active():
                raise ValueError(f"Product is not active")
            if quantity > product.get_quantity():
                raise ValueError(f"Not enough quantity available")
            total_price += product.buy(quantity)
        return total_price
