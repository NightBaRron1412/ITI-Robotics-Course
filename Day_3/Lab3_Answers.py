# Parent class
class Vehicle:
    # instance attributes
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

# Child class
class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, capacity = 50):
        super().__init__(name, max_speed, mileage)
        self.capacity = capacity

    def seating_capacity(self):
        return f"The seating capacity of a {self.name} is {self.capacity} passengers"

    def fare(self):
        return self.capacity * 100.0