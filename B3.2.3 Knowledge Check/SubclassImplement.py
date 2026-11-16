from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def display_specs(self):
        return f"{self.brand} - Max Speed: {self.max_speed}"

    @abstractmethod
    def calculate_fuel_Needed(self, distance):
        pass

    @abstractmethod
    def start_engine(self, key_code):
        pass

class Car(Vehicle):
    def __init__(self, brand, max_speed, mpg):
        super().__init__(brand, max_speed)
        self.mpg = mpg

    def calculate_fuel_Needed(self, distance):
        return distance / self.mpg

    def start_engine(self, key_code):
        if key_code == 1234:
            return "Engine started"
        return "Invalid key"

def main():
    my_car = Car("Toyota", 120, 30)
    print(my_car.display_specs())
    print(my_car.calculate_fuel_Needed(150))
    print(my_car.start_engine(1234))

if __name__ == "__main__":
    main()