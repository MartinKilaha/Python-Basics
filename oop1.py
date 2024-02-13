class Fruits:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        print(f" I love {self.name} because they are cheap, they cost {self.price}")


mygrocery = Fruits("banana", 5)
mygrocery.display()
mygrocery1 = Fruits("pineapple", 10)
mygrocery1.display()
mygrocery2 = Fruits("oranges", 40)
mygrocery2.display()
mygrocery3 = Fruits("grapes", 60)
mygrocery3.display()
mygrocery4 = Fruits("strawberry", 150)
mygrocery4.display()
mygrocery5 = Fruits("watermelon", 250)
mygrocery5.display()
