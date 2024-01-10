# YOUR SOLUTION
class Pizza:
    def __init__(self, size, topping, sauce):
        self.size = size
        self.topping = topping
        self.sauce = sauce

    def __str__(self):
        return f"{self.size} Pizza with {self.topping} and {self.sauce} sauce"


pizza1 = Pizza(size=50, topping="Quattro Formaggi", sauce="olive oil")
pizza2 = Pizza(size=32, topping="Prosciutto", sauce="garlic sauce")
pizza3 = Pizza(size=40, topping="Margheritta", sauce="tomato sauce")

print(pizza1)
print(pizza2)
print(pizza3)