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