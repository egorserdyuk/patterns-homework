# This is one of the variations of the three design patterns in airport routing program
from __future__ import annotations
from abc import ABC, ABCMeta, abstractmethod
from typing import Dict, List
from random import randint

# Strategy implementation
class RouteContext():
    def __init__(self, strategy: RouteStrategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: RouteStrategy):
        self._strategy = strategy

    def logic(self):
        print("Context: Sorting data using the strategy")
        result = self._strategy.analyze({'Bicycle': randint(60, 120),'Car': randint(10, 40),'Taxi': randint(20, 60),'Bus': randint(60, 180)})
        for i in result:
	        print(f'{i[0]} on time is around {i[1]} minutes')

class RouteStrategy(ABC):
    @abstractmethod
    def analyze(self, data: Dict):
        pass

class Fastest(RouteStrategy):
    def analyze(self, data: Dict):
        return sorted(data.items(), key=lambda x: x[1])

class Slowest(RouteStrategy):
    def analyze(self, data: Dict):
        return sorted(data.items(), key=lambda x: x[1], reverse=True)

# Decorator implementation
class Price:
    __metaclass__ = ABCMeta

    def __init__(self):
        self._transport = "Unkonwn price for unknown transport"

    def get_price(self):
        return self._transport

    @abstractmethod
    def price(self):
        pass

# Singleton implementation
class DataView(object):
    instance = None
    params = []
    
    def __new__(cls):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance

    def set(cls, key, value):
        cls.params[key] = value
        return cls.params

    def get(cls, key):
        return cls.params[key]

if __name__ == "__main__":
    context = RouteContext(Fastest())
    print("Client: Strategy is set to the fastest sorting\n")
    context.logic()

    print("\nClient: Strategy is set to the slowest sorting\n")
    context.strategy = Slowest()
    context.logic()

    # data_store = DataView()
    # data_store.set('0', 'old')
    # print(data_store.get(0))
