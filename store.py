import products


class Store:
    """
    A class to represent a store that contains a list of products
    and allows various operations on them.

    Attributes:
    product_list (list): A list of products available in the store.
    """
    def __init__(self, product_list):
        """
        Initialize the Store with a list of products.

        Parameters:
        product_list (list): The initial list of products available
                             in the store.
        """
        self.product_list = product_list

    def add_product(self, product):
        """
        Add a product to the store.

        Parameters:
        product (Product): The product to add to the store.
        """
        self.product_list.append(product)

    def remove_product(self, product):
        """
        Remove a product from the store.

        Parameters:
        product (Product): The product to remove from the store.
        """
        if product in self.product_list:
            self.product_list.remove(product)

    def get_total_quantity(self):
        """
        Get the total quantity of all products in the store, excluding
        non-stocked and limited products that do not have a defined
        stock quantity.

        Returns:
        int: The total quantity of items in the store.
        """
        total_quantity = 0
        for product in self.product_list:
            if not isinstance(product, products.NonStockedProduct):
                total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self):
        """
        Get a list of all active products in the store.

        Returns:
        list: A list of active products in the store.
        """
        all_active_products = []
        for product in self.product_list:
            if product.is_active():
                all_active_products.append(product)
        return all_active_products

    def order(self, shopping_list):
        """
        Place an order for a list of products and return the total
        price.

        Parameters:
        shopping_list (list): A list of tuples, where each tuple
                              contains a product and the quantity
                              to buy.

        Returns:
        float: The total price of the order.

        Raises:
        ValueError: If the product is not active or if the requested
                    quantity exceeds available stock.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            try:
                if not product.is_active():
                    raise ValueError(
                        f"Product '{product.name}' is not active and "
                        f"cannot be ordered.")
                if isinstance(product, products.NonStockedProduct):
                    total_price += product.buy(quantity)
                elif quantity > product.get_quantity():
                    raise ValueError(
                        f"Not enough quantity available for '{product.name}'. "
                        f"Available: {product.get_quantity()}, "
                        f"Requested: {quantity}")
                else:
                    total_price += product.buy(quantity)
            except ValueError as e:
                print(f"Error: {str(e)}")
                continue
        return total_price
