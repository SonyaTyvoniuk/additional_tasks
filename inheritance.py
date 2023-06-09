class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight

    def start_engine(self):
        print("The vehicle's engine is starting...")


class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors, num_passengers):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors
        self.num_passengers = num_passengers

    def start_engine(self):
        print("The car's engine is starting...")

    def drive(self):
        print("The car is being driven.")


class Truck(Vehicle):
    def __init__(self, make, model, year, weight, cargo_capacity, towing_capacity):
        super().__init__(make, model, year, weight)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity

    def start_engine(self):
        print("The truck's engine is starting...")

    def haul(self):
        print("The truck is hauling.")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, weight, num_wheels, has_sidecar):
        super().__init__(make, model, year, weight)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar

    def start_engine(self):
        print("The motorcycle's engine is starting...")

    def ride(self):
        print("The motorcycle is being ridden.")


# Створюємо екземпляри об'єктів
car = Car("Toyota", "Camry", 2022, 1500, 4, 5)
truck = Truck("Ford", "F-150", 2021, 3000, 5000, 10000)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2020, 500, 2, False)

# Викликаємо відповідні методи для кожного об'єкта
car.start_engine()
car.drive()

truck.start_engine()
truck.haul()

motorcycle.start_engine()
motorcycle.ride()
