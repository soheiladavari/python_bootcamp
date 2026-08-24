#5
warehouse = {
"electronics": {
"phone": {"price_range": (8000000, 25000000), "suppliers": 
{"digikala", "torob"}},
"laptop": {"price_range": (15000000, 60000000), "suppliers": 
{"digikala", "emalls"}},
},
"furniture": {
"chair": {"price_range": (500000, 3000000), "suppliers": {"emalls", 
"sofra"}},
 },
}
def has_overlap(price_range, user_range):
    try:
        if len(price_range) != 2 or len(user_range) != 2:
            raise ValueError("Price range must contain exactly two values.")

        start1, end1 = price_range
        start2, end2 = user_range

        if start1 > end1 or start2 > end2:
            raise ValueError("Start price cannot be greater than end price.")

        return max(start1, start2) <= min(end1, end2)

    except (TypeError, ValueError) as error:
        print(f"Error: {error}")
        return False
def get_user_range():
    try:
        minimum = int(input("Enter minimum price: "))
        maximum = int(input("Enter maximum price: "))

        if minimum < 0 or maximum < 0:
            raise ValueError("Price cannot be negative.")

        if minimum > maximum:
            raise ValueError("Minimum price cannot be greater than maximum price.")

        return (minimum, maximum)

    except ValueError as error:
        print(f"Invalid input: {error}")
        return None
def find_overlapping_products(warehouse, user_range):
    result = []

    for category, products in warehouse.items():
        for product, information in products.items():

            price_range = information["price_range"]

            if has_overlap(price_range, user_range):
                result.append((category, product))

    return result
def get_unique_suppliers(warehouse):
    try:
        return {
            category: set().union(
                *(product["suppliers"] for product in products.values())
            )
            for category, products in warehouse.items()
        }

    except (KeyError, TypeError) as error:
        print(f"Error: {error}")
        return {}
def main():

    # Part A
    user_range = get_user_range()

    if user_range is not None:

        overlapping = find_overlapping_products(
            warehouse,
            user_range
        )

        if overlapping:
            print("\nProducts with overlapping price range:")

            for category, product in overlapping:
                print(f"{category} -> {product}")
        else:
            print("\nNo overlapping products found.")
print("\nUnique suppliers by category:")

suppliers = get_unique_suppliers(warehouse)

for category, supplier_set in suppliers.items():
        print(f"{category}: {supplier_set}")


main()