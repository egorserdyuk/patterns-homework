# This is one of the variations of the three design patterns in airport routing program
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import List
from random import randint

# Strategy implementation
class Route:  
    __metaclass__ = ABCMeta
    transport_type = None

    @abstractmethod
    def display(self):
        pass

    def time(self):
        self.transport_type.time()

    def set_transport(self, transport_type):
        self.transport_type = transport_type

class Bicycle(Route):
    def __init__(self):
        self.transport_type = BicycleTime()

class Car(Route):
    def __init__(self):
        self.transport_type = CarTime()

class Taxi(Route):
    def __init__(self):
        self.transport_type = TaxiTime()

class Bus(Route):
    def __init__(self):
        self.transport_type = BusTime()


class TransportType:
    __metaclass__ = ABCMeta

    @abstractmethod
    def time(self):
        pass

class BicycleTime(TransportType):
    def time(self):
        print(f'Around {randint(60, 120)} minutes by Bicycle')

class CarTime(TransportType):
    def time(self):
        print(f'Around {randint(10, 40)} minutes by Car')

class TaxiTime(TransportType):
    def time(self):
        print(f'Around {randint(20, 60)} minutes by Taxi')

class BusTime(TransportType):
    def time(self):
        print(f'Around {randint(60, 180)} minutes by Bus')

# Decorator implementation
class Price:
    __metaclass__ = ABCMeta

    def __init__(self):
        self._transport = "Unkonwn price for unknow transport"

    def get_price(self):
        return self._transport

    @abstractmethod
    def price(self):
        pass

# Singleton implementation
class DataViewerMeta(type):  
    _instances = {}

    def __call__(self, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class DataViewerBicycle(metaclass=DataViewerMeta):
    def fetch_data(self):
        way_bicycle = Bicycle()

class DataBicycle(object):
    instance = None
    
    def __new__(cls):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

if __name__ == "__main__":
    way_bicycle = Bicycle()
    way_car = Car()
    way_bus = Bus()

    way_bicycle.time()
    way_car.time()
    way_bus.time()

    data_way_bycicle_1 = DataBicycle(way_bicycle)
    data_way_bycicle_2 = DataBicycle(way_bicycle)

    print(data_way_bycicle_1)
    print(data_way_bycicle_2)

    assert data_way_bycicle_1 == data_way_bycicle_2, "Something wents wrong"
