class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"Driving the {self.brand} {self.model}")


class ElectricEngine:
    # @staticmethod
    @staticmethod
    def charge():
        print("Charging the electric engine")

class HybridCar(Vehicle, ElectricEngine):
    def __init__(self, brand, model):
        Vehicle.__init__(self, brand, model)

    def drive(self):
        print(f"Driving the {self.brand} {self.model} in hybrid mode")


tiago = HybridCar("Tiago", "1.0")
tiago.charge()
tiago.drive()
