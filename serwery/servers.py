#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from itertools import product
from typing import Optional, List, Dict
import re
from abc import ABC, abstractmethod
 
pattern = r'[a-zA-Z]*/d{1,3}'
re.compile(pattern)
 
class Product:
    def __init__(self, product_name: str, product_price: float):
        self.product_name = product_name
        self.product_price = product_price
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)
    #dodać property do product name w celu wersyfikacji porpawnosci nadania nazwy
    
    def __eq__(self, other) -> bool:
        return True if (self.product_price == other.product_price) and (self.product_name == other.product_name) else False
 
    def __hash__(self):
        return hash((self.name, self.price))

    @property
    def product_name(self):
        return self._product_name

    @product_name.setter
    def product_name(self, value: str):
        if pattern.fullmatch(value):
            self._product_name = value
        else:
            raise ValueError
 
 
class TooManyProductsFoundError(Exception):
    # Reprezentuje wyjątek związany ze znalezieniem zbyt dużej liczby produktów.
    pass
 
 
# FIXME: Każada z poniższych klas serwerów powinna posiadać:
#   (1) metodę inicjalizacyjną przyjmującą listę obiektów typu `Product` i ustawiającą atrybut `products` zgodnie z typem reprezentacji produktów na danym serwerze,
#   (2) możliwość odwołania się do atrybutu klasowego `n_max_returned_entries` (typu int) wyrażający maksymalną dopuszczalną liczbę wyników wyszukiwania,
#   (3) możliwość odwołania się do metody `get_entries(self, n_letters)` zwracającą listę produktów spełniających kryterium wyszukiwania
 
class Server(ABC):
    n_max_returned_entries = 3

    @abstractmethod
    def __init__(self, products: List[Product]) -> None:
        pass

    @abstractmethod
    def get_entries(self, n_letters: int) -> List[Product]:
        pass

class ListServer:
    def __init__(self, products: List[Product]) -> None:
        self.products = products
        
    def get_entries(self, n_letters: int) -> List[Product]:
        pass
 
class MapServer:
    def __init__(self, products: List[Product]) -> None:
        self.products = {product.name : product for product in products}

    def get_entries(self, n_letters: int) -> List[Product]:
        pass
    
 
class Client:
    def __init__(self, server: Server):
        self.server = server
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą obiekt reprezentujący serwer
 
    def get_total_price(self, n_letters: Optional[int]) -> Optional[float]:
        raise NotImplementedError()