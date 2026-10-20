#2
class Product:
    shop_name="ShopHub"
    increase_rate=1.05

    def __init__(self,title,category,price):
        self.title=title
        self.category=category
        self.price=price

    def info(self):
        return f"{self.title}({self.category})"

    def increase_price(self):
        self.price*=Product.increase_rate
        # self.price*=type(self).increase_rate
        return f"increased price: {self.price}"
    @classmethod
    def create_object(cls, product):
        title,category,price=product.split("-")
        price=float(price)
        return cls(title,category,price)

    @staticmethod
    def is_open(day):
        # if day=="friday":
        #     return False
        # return True
        return day !="friday"

    @classmethod
    def change_rate(cls,new_rate):
        cls.increase_rate=new_rate

p1=Product("laptop","digital",8000)
print(p1.info())
p2=Product.create_object("Ipad-digital-5000")
print(p2.info())
print("brfore:",p1.price)
p1.increase_price()
print("after:", p1.price)
Product.change_rate(1.10)
print(p2.increase_price())



    
    


        