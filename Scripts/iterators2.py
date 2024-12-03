class Fibonacci:
    def __init__(self, n:int):
        self.n = n
        
    def __iter__(self):
        return FibonacciIterator(self.n)
    
class FibonacciIterator:
    def __init__(self, n:int):
        self.n = n
        self.current, self.next = 0, 1
        
    def __next__(self) -> int:
        if self.n<0:
            raise StopIteration()
        self.n -=1
        current = self.current
        self.current, self.next = self.next, self.next+current
        return current
    
    def __iter__(self):
        return self
    
fibo = Fibonacci(10)
iterator = iter(fibo)
print(isinstance(iterator, FibonacciIterator))
for number in fibo:
    print(number)
    
class SquareNumbers:
    def __init__(self,n):
        self.n = n
        
    def __getitem__(self, index: int):
        if index < 0 or index>self.n:
            raise IndexError
        return index * index

print(list(SquareNumbers(100)))

from random import choice
from collections.abc import Iterable
iterator = iter(lambda: choice(['?','!','a','c','%']), '?')
print("".join(iterator))

from enum import Enum, auto

class Color(Enum):
    RED = 'красни'
    GREEN = 'зелёны'
    BLUE = 'сини'
    BLACK = 'чёрний'
    WHITE = 'бели'
    
print(isinstance(Color, Iterable))
print([color.value for color in Color])

from itertools import count, cycle, islice

numbers = count(start=1, step=1)
fizzes = cycle(["","","fizz"])
buzzes = cycle(["","","","","buzz"])
fizzbuzzes = islice(zip(numbers, fizzes, buzzes), 10)

for number, fizz, buzz in fizzbuzzes:
    print(f"{fizz}{buzz}" or number)
        
import time 
def do(n):
    time.sleep(1)
    return n * n

tasks = [1,2,3,4,5,6,7,8,9,10,11,12]

t0 = time.perf_counter()

result = list(map(do,tasks))
print(result)
print('time', int(time.perf_counter()-t0), 'sec')

import sys
name = sys.stdin.readline().strip()
print("name: ", name)