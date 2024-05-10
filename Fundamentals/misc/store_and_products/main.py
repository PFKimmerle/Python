from product import Product
from store import Store


if __name__ == "__main__":
    store = Store("Tech Gadgets")

    # Create some product instances
    product1 = Product("Laptop", 1200, "Electronics", 101)
    product2 = Product("Smartphone", 700, "Electronics", 102)
    product3 = Product("Headphones", 150, "Accessories", 103)

    # Add products to the store
    store.add_product(product1)
    store.add_product(product2)
    store.add_product(product3)

    # Testing methods
    store.inflation(5)
    store.set_clearance("Accessories", 10)
    store.sell_product(102)
    product1.print_info()
    product3.print_info()