from typing_extensions import override
from abc import ABC, abstractmethod
import math


class Vehicle:
    def __init__(self, name: str, base_fee: float):
        self.name = name
        self.base_fee = base_fee

    def trip_cost(self, distance_km: float):
        return self.base_fee

    def __str__(self):
        return f"The car: {self.name} base fee: {self.base_fee}"


class GasCar(Vehicle):
    def __init__(self, liters_per_100km: float, price_per_liter: float, base_fee: float):
        super().__init__("GasCar", base_fee)
        self.liters_per_100km = liters_per_100km
        self.price_per_liter = price_per_liter

    @override
    def trip_cost(self, distance_km: float):
        fuel_used = (distance_km / 100) * self.liters_per_100km
        return self.base_fee + fuel_used * self.price_per_liter

    @override
    def __str__(self):
        return f"{super().__str__()}, liters_per_100km: {self.liters_per_100km}, price_per_liter: {self.price_per_liter}"



class ElectricCar(Vehicle):
    def __init__(self, kwh_per_100km: float, price_per_kwh: float, base_fee: float):
        super().__init__("ElectricCar", base_fee)
        self.kwh_per_100km = kwh_per_100km
        self.price_per_kwh = price_per_kwh

    @override
    def trip_cost(self, distance_km: float):
        energy_used = (distance_km / 100) * self.kwh_per_100km
        return self.base_fee + energy_used  * self.price_per_kwh

    @override
    def __str__(self):
        return f"{super().__str__()}, kwh_per_100km: {self.kwh_per_100km}, price_per_kwh: {self.price_per_kwh}"


class Taxi(Vehicle):
    def __init__(self, price_per_km: float, is_night: bool, base_fee: float):
        super().__init__("Taxi", base_fee)
        self.price_per_km = price_per_km
        self.is_night = is_night

    @override
    def trip_cost(self, distance_km: float):
        cost = self.base_fee + distance_km * self.price_per_km
        if self.is_night:
            cost *= 1.2
        return cost

    @override
    def __str__(self):
        return f"{super().__str__()}, price_per_km: {self.price_per_km}, is_night: {self.is_night}"




gas1 = GasCar(7.2, 7.1, 5)
print(gas1.trip_cost(50))
print(gas1)

elec1 = ElectricCar(16, 1.2, 5)
print(elec1.trip_cost(50))
print(elec1)

taxi1 = Taxi(3.8, True, 12)
print(taxi1.trip_cost(50))
print(taxi1)
