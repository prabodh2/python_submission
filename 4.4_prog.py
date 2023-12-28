class Store:
    def __init__(self):
        # Dictionary to store product codes and prices
        self.products = {
            '001': {'name': 'Product A', 'price': 10.0},
            '002': {'name': 'Product B', 'price': 20.0},
            '003': {'name': 'Product C', 'price': 15.0},
        }

    def display_menu(self):
        print("Product Code\tProduct Name\tPrice")
        for code, details in self.products.items():
            print(f"{code}\t\t{details['name']}\t\t${details['price']}")

    def generate_bill(self, quantities):
        total_amount = 0.0
        print("\nBilling Details:")
        print("Product Code\tProduct Name\tPrice\tQuantity\tTotal")
        for code, details in self.products.items():
            quantity = quantities.get(code, 0)
            if quantity > 0:
                total = details['price'] * quantity
                total_amount += total
                print(f"{code}\t\t{details['name']}\t\t${details['price']}\t{quantity}\t\t${total}")
        print("\nTotal Amount: ${:.2f}".format(total_amount))

# Example usage:
def main():
    store = Store()

    # Display menu
    print("Welcome to the Store!")
    store.display_menu()

    # Prompt user to enter quantity for each product
    quantities = {}
    for code in store.products.keys():
        quantity = int(input(f"Enter the quantity of {store.products[code]['name']} (Product Code {code}): "))
        quantities[code] = quantity

    # Generate and display the bill
    store.generate_bill(quantities)

if __name__ == "__main__":
    main()
