#4
from math import gcd
class Fraction:
    def __init__(self,numerator,denominator):
        if denominator==0:
            raise ValueError("denominator cannot be zero")
        elif denominator<0:
            numerator=-numerator
            denominator=-denominator
        g=gcd(numerator,denominator)
        numerator//=g
        denominator//=g

        self.numerator=numerator
        self.denominator=denominator
        
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"