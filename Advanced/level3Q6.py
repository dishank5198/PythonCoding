# Single Inheritance
class Shape:
    def __init__(self, num_side):
        self.num_side = num_side

    def sides(self):
        print("It has {num} sides".format(num = self.num_side))


class Triangle(Shape):
    def sides(self):
        print("It has 3 sides")


tri = Triangle(3)
tri.sides()


# Multiple Inheritance
class Walker:
    def walk(self):
        return "I can walk."

class Swimmer:
    def swim(self):
        return "I can swim."

class Person(Walker, Swimmer):
    def __init__(self, name):
        self.name = name

    def abilities(self):
        walk_ability = self.walk()
        swim_ability = self.swim()
        return "{name}: {walk} and {swim}".format(name = self.name, walk = walk_ability, swim = swim_ability)

person = Person("Dishank")
print(person.abilities())


# Multilevel Inheritance
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        return "Brand: {brand}".format(brand=self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def car_info(self):
        return "{info}, Model: {model}".format(info=self.info(), model=self.model)


class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def battery_info(self):
        return "{car_info}, Battery Capacity: {battery} kWh".format(car_info=self.car_info(),battery=self.battery_capacity)


tesla = ElectricCar("Tesla", "Model S", 100)
print(tesla.battery_info())