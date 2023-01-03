import numpy as np
import scipy
import pickle
import typing
import math
import types
import pickle
from inspect import isfunction
from typing import Union, List, Tuple

def fun(x):
    return np.exp(-2*x)+x**2-1

def dfun(x):
    return -2*np.exp(-2*x) + 2*x

def ddfun(x):
    return 4*np.exp(-2*x) + 2

def bisection(a: Union[int,float], b: Union[int,float], f: typing.Callable[[float], float], epsilon: float, iteration: int) -> Tuple[float, int]:
    '''funkcja aproksymująca rozwiązanie równania f(x) = 0 na przedziale [a,b] metodą bisekcji.

    Parametry:
    a - początek przedziału
    b - koniec przedziału
    f - funkcja dla której jest poszukiwane rozwiązanie
    epsilon - tolerancja zera maszynowego (warunek stopu)
    iteration - ilość iteracji

    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    if type(a) in [int , float] and type(b) in [int, float] and type(iteration) is int \
        and type(epsilon) is float and callable(f):
        
        if f(a)*f(b) < 0:
            for i in range(iteration):
                x_root = (a + b) / 2
                root = f(x_root)
                if f(a) * root < 0:
                    b = x_root
                elif f(b) * root < 0:
                    a = x_root
                elif np.abs(root) < epsilon or np.abs(b - a) < epsilon:
                    return x_root, i
            return x_root, iteration
    else:
        return None
    

def secant(a: Union[int,float], b: Union[int,float], f: typing.Callable[[float], float], epsilon: float, iteration: int) -> Tuple[float, int]:
    '''funkcja aproksymująca rozwiązanie równania f(x) = 0 na przedziale [a,b] metodą siecznych.

    Parametry:
    a - początek przedziału
    b - koniec przedziału
    f - funkcja dla której jest poszukiwane rozwiązanie
    epsilon - tolerancja zera maszynowego (warunek stopu)
    iteration - ilość iteracji

    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    if type(a) in [int , float] and type(b) in [int, float] and type(iteration) is int \
        and type(epsilon) is float and callable(f):
        if f(a)*f(b) < 0:
            for i in range(iteration):
                x_root = b - (f(b) * (b - a))/(f(b) - f(b))
                root  = f(x_root)
                if np.abs(root) < epsilon:
                    return x_root, i
                elif f(a) * root < 0:
                    b = x_root
                elif f(b) * root < 0:
                    a = x_root
                elif np.abs(b - a) < epsilon:
                    return x_root, i
            return b - (f(b) * (b - a))/(f(b) - f(b)), iteration
    else:
        return None
    
    
def check_constant_sign(interval: np.ndarray) -> bool:
    if all(np.sign(interval) < 0) or all(np.sign(interval) > 0):
        return True
    return False

def newton(f: typing.Callable[[float], float], df: typing.Callable[[float], float], ddf: typing.Callable[
    [float], float], a: Union[int,float], b: Union[int,float], epsilon: float, iteration: int) -> Tuple[float, int]:
    ''' Funkcja aproksymująca rozwiązanie równania f(x) = 0 metodą Newtona.
    Parametry: 
    f - funkcja dla której jest poszukiwane rozwiązanie
    df - pochodna funkcji dla której jest poszukiwane rozwiązanie
    ddf - druga pochodna funkcji dla której jest poszukiwane rozwiązanie
    a - początek przedziału
    b - koniec przedziału
    epsilon - tolerancja zera maszynowego (warunek stopu)
    Return:
    float: aproksymowane rozwiązanie
    int: ilość iteracji
    '''
    if type(a) in [int , float] and type(b) in [int, float] and type(iteration) is int \
        and type(epsilon) is float and callable(f) and callable(df) and callable(ddf):
        #sprawdzanie stałości znaku pochodnych w przedziale
        interval_ab = np.linspace(a,b,100)
        y_df = df(interval_ab)
        y_ddf = ddf(interval_ab)
        if not check_constant_sign(y_df) and not check_constant_sign(y_ddf):
            return None
        
        x = a
    
        if f(a) * f(b) < 0:
            for i in range(iteration):
                x_root = x - f(x) / df(x)
                if np.abs(x_root - x) < epsilon:
                    return x_root, i
                x = x_root
            return x_root, iteration    
    else:
        return None