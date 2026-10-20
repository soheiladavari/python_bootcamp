#1
class Book:
    book_count=0
    def __init__(self, title, author, pages,price):

        self.title=title
        self.author=author
        self.pages=pages
        self.price=price
        Book.book_count+=1

    #instance method
    def discount(self,percent):
        self.price=self.price*(1-percent/100)
        return self.price

    
    @classmethod
    def book_counter(cls):
        return cls.book_count
    
    #we could use instance method too. that would check if an object is expensive or not.
    @staticmethod
    def is_expensive(price):
        return  price>200000

    def book_info(self):
        return f"title: {self.title}, author: {self.author} ,pages: {self.pages}, price: {self.price}"

b1=Book("math","james",420,370000)
b2=Book("literature","adam",540,170000)
b3=Book("physics","david",520,300000)
print(b1.discount(20))
print(Book.book_counter())
print(b1.book_info())  
print(Book.is_expensive(350000))      