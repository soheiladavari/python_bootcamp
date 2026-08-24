#3
products = [
{"name": "Keyboard", "price": 500000, "in_stock": True},
{"name": "Mouse", "price": 200000, "in_stock": False},
{"name": "Monitor", "price": 3500000, "in_stock": True},
{"name": "Webcam", "price": 800000, "in_stock": True},
]
from functools import reduce

print(reduce(lambda x,y:x+y , list(map(
    lambda y:y["price"]*0.9,filter(
        lambda x:x["in_stock"]==True, products)))))
print(f"price: {[f'{x["price"]:.2f}' for x in products]}")