class Cars:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def onyesha(self):
        print(f"My dream car is a {self.color} {self.make} and my model is {self.model} manufactured in {self.year}")


myobj = Cars("Toyota", "Vitz", 2020, "red")
myobj.onyesha()
myobj1 = Cars("Mercedes", "S_class", 2023, "jungle green")
myobj1.onyesha()
