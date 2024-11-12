import products
import promotions
import store


def show_menu():
    """Display menu options."""
    menu_options = [
        "1. List all products in store",
        "2. Show total amount in store",
        "3. Make an order",
        "4. Quit"
    ]
    print("\n   Store Menu")
    print("   ----------")
    for option in menu_options:
        print(option)


def list_store_products(store_inst):
    """List products in store."""
    products_in_store = store_inst.get_all_products()
    print("------")
    for num, product in enumerate(products_in_store):
        print(f"{num + 1}. {product.show()}")
    print("------")


def show_total_amount(store_inst):
    """Display available quantity."""
    total_amount = store_inst.get_total_quantity()
    print(f"Total of {total_amount} items in store")


def get_valid_product_choice(products_in_store):
    """Prompt user for a valid product choice from the list of available products."""
    while True:
        product_order = input("Which product # do you want? ")
        if product_order == "":
            return None
        try:
            product_order = int(product_order) - 1
            if 0 <= product_order < len(products_in_store):
                return products_in_store[product_order]
            else:
                print("Invalid product number, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")


def get_valid_quantity(product):
    """Prompt user for a valid quantity for the selected product."""
    while True:
        order_amount = input(
            f"What amount do you want for '{product.name}'? ")
        if order_amount == "":
            print("Please enter a valid quantity.")
            continue
        try:
            order_amount = int(order_amount)
            if order_amount <= 0:
                print(
                    "Quantity must be greater than zero, please try again.")
                continue
            if isinstance(product,
                          products.LimitedProduct) and order_amount > product.max_quantity_per_order:
                print(
                    f"Cannot buy more than {product.max_quantity_per_order} units of '{product.name}' per order.")
                continue
            if product.get_quantity() < order_amount:
                print(
                    f"Not enough quantity available for '{product.name}'. Available: {product.get_quantity()}, Requested: {order_amount}")
                continue
            return order_amount
        except ValueError:
            print("Invalid quantity, please enter a valid number.")


def get_valid_quantity_unlimited(product):
    """Prompt user for a valid quantity for the selected product with unlimited availability."""
    while True:
        order_amount = input(
            f"What amount do you want for '{product.name}'? (Unlimited quantity available) ")
        if order_amount == "":
            print("Please enter a valid quantity.")
            continue
        try:
            order_amount = int(order_amount)
            if order_amount <= 0:
                print(
                    "Quantity must be greater than zero, please try again.")
                continue
            return order_amount
        except ValueError:
            print("Invalid quantity, please enter a valid number.")


def make_order(store_inst):
    """Ask user to order product and quantity. Create a shopping list. Return the total payable amount."""
    products_in_store = store_inst.get_all_products()
    shopping_list = []

    list_store_products(store_inst)
    print("When you want to finish order, enter empty text.")

    while True:
        product = get_valid_product_choice(products_in_store)
        if product is None:
            break

        # Check if product is a NonStockedProduct to allow unlimited purchases
        if isinstance(product, products.NonStockedProduct):
            order_amount = get_valid_quantity_unlimited(product)
        else:
            order_amount = get_valid_quantity(product)

        shopping_list.append((product, order_amount))
        print("Product added to list!\n")

    if shopping_list:
        try:
            total_payment = store_inst.order(shopping_list)
            print("********")
            print(f"Order made! Total payment: ${total_payment:.2f}")
        except ValueError:
            print(
                "Error while making order! Quantity larger than what exists")


def start(store_inst):
    """Prompt user with menu options. Ask user to choose action."""
    options_table = {
        "1": list_store_products,
        "2": show_total_amount,
        "3": make_order,
        "4": exit
    }

    while True:
        show_menu()
        choice = input("Please choose a number: ")
        action = options_table.get(choice)

        if action:
            action(store_inst)
        else:
            print("Invalid choice, please try again.")


def main():
    """Main function to run the program."""
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250,
                         quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
        products.NonStockedProduct("Windows License", price=125),
        products.LimitedProduct("Shipping", price=10, quantity=250,
                                max_quantity_per_order=1)
    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice(
        "Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!",
                                                percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
