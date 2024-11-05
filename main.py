import products
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


def make_order(store_inst):
    """Ask user to order product and quantity. Create a shopping
    list. Return the total payable amount."""
    products_in_store = store_inst.get_all_products()
    shopping_list = []
    list_store_products(store_inst)
    print("When you want to finish order, enter empty text.")
    while True:
        product_order = (input("Which product # do "
                               "you want? "))
        order_amount = (input("What amount do you "
                              "want? "))
        if product_order == "" or order_amount == "":
            break
        try:
            product_order = int(product_order) - 1
            order_amount = int(order_amount)
            if product_order < 0 or product_order >= len(
                    products_in_store):
                continue
            shopping_list.append((products_in_store[
                                      product_order],
                                  order_amount))
            print("Product added to list!\n")
        except ValueError:
            print("Error adding product!\n")
    if shopping_list:
        try:
            total_payment = store_inst.order(shopping_list)
            print("********")
            print(f"Order made! Total payment: $"
                  f"{total_payment:.2f}")
        except ValueError:
            print("Error while making order! Ordered quantity "
                  "exceeds stock availability")


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
        choice = input(f"Please choose a number: ")
        action = options_table.get(choice)

        if action:
            action(store_inst)


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
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
