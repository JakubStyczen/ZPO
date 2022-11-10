#!/usr/bin/python
# -*- coding: utf-8 -*-
 
from itertools import product
from typing import Optional, List, Dict
import re
from abc import ABC, abstractmethod
 

 
class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    # FIXME: klasa powinna posiadać metodę inicjalizacyjną przyjmującą argumenty wyrażające nazwę produktu (typu str) i jego cenę (typu float) -- w takiej kolejności -- i ustawiającą atrybuty `name` (typu str) oraz `price` (typu float)
    
    def __eq__(self, other) -> bool:
        return True if (self.price == other.price) and (self.name == other.name) else False
 
    def __hash__(self):
        return hash((self.name, self.price))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        pattern = r'[a-zA-Z]+\d{1,3}'
        pattern = re.compile(pattern)
        if pattern.fullmatch(value):
            self._name = value
        else:
            raise ValueError
 
 
class ServerError(Exception):
    pass
 
class TooManyProductsFoundError(ServerError):
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
        raise NotImplementedError

    @abstractmethod
    def get_entries(self, n_letters: int) -> List[Product]:
        raise NotImplementedError
    
    def sort_products(self, products: List[Product]) -> List[Product]:
        func = lambda prod: prod.price
        return sorted(products, key=func)

    def match_product(self, n_letters: int, product: Product, matched_products: List[Product]) -> None:
        pattern = pattern = f'[a-zA-Z]{{{n_letters}}}\d{{1,3}}'
        if re.fullmatch(pattern, product.name):
            if len(matched_products) + 1 <= self.n_max_returned_entries:
                matched_products.append(product)
            else:
                raise TooManyProductsFoundError 


class ListServer(Server):
    def __init__(self, products: List[Product]) -> None:
        self.products = products
        
    def get_entries(self, n_letters: int = 1) -> List[Product]:
        filtered_products = []
        for product in self.products:
            self.match_product(n_letters, product, filtered_products)
        return self.sort_products(filtered_products)         
 
 
 
class MapServer(Server):
    def __init__(self, products: List[Product]) -> None:
        self.products = {product.name : product for product in products}

    #Jak to z nazwami w słowniku??
    def get_entries(self, n_letters: int = 1) -> List[Product]:
        filtered_products = []
        for product in self.products.values():
            self.match_product(n_letters, product, filtered_products)
        return self.sort_products(filtered_products)  
    
 
class Client:
    def __init__(self, server: Server) -> None:
        self.server = server
 
    def get_total_price(self, n_letters: Optional[int] = 1) -> Optional[float]:
        try:
            if n_letters is None:
                entries_products = self.server.get_entries()
            else:
                entries_products = self.server.get_entries(n_letters)
            
            return sum([product.price for product in entries_products]) if entries_products else None
        except TooManyProductsFoundError:
            return None
    
