class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_price(self):
        return self.price * self.quantity


class Bill:
    TAX_RATE = 0.18   # 18% GST

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        return sum(p.total_price() for p in self.products)

    def calculate_tax(self):
        return self.calculate_subtotal() * self.TAX_RATE

    def calculate_grand_total(self):
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self):
        print("\n================= FINAL BILL =================")
        print("{:<20} {:<10} {:<10} {:<10}".format("Product", "Price", "Qty", "Total"))
        print("--------------------------------------------------------")
        for p in self.products:
            print("{:<20} {:<10} {:<10} {:<10}".format(
                p.name, p.price, p.quantity, p.total_price()
            ))
        print("--------------------------------------------------------")
        print(f"Subtotal: ₹{self.calculate_subtotal():.2f}")
        print(f"GST (18%): ₹{self.calculate_tax():.2f}")
        print(f"Grand Total: ₹{self.calculate_grand_total():.2f}")
        print("========================================================\n")


# -------- Main Program --------
bill = Bill()

while True:
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    product = Product(name, price, quantity)
    bill.add_product(product)

    choice = input("Add more items? (y/n): ").lower()
    if choice != 'y':
        break

bill.display_bill()
