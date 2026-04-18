# Build a program that raises a ProductNotFoundException when a product is not present in a product list.
# Custom Exception
class ProductNotFoundException(Exception):
    pass


def find_product(product_list, product_name):
    if product_name not in product_list:
        raise ProductNotFoundException(f"{product_name} not found in the product list.")
    else:
        print(f"{product_name} is available in the product list.")


# Product list
products = ["Laptop", "Mobile", "Tablet", "Headphones"]

try:
    user_product = input("Enter product name to search: ")
    find_product(products, user_product)

except ProductNotFoundException as e:
    print("Custom Exception:", e)

finally:
    print("Program execution completed.")