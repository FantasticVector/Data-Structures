# Brute Force
def fibonacci(n):
  if n <= 2:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

import inspect
def stack_depth():
  return len(inspect.getouterframes(inspect.currentframe())) -1

# Top Down

def fibonacci(n):
  print('{indent}fibonacci({n}) called'.format(indent=' '*stack_depth(), n=n))
  if n <= 2:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

# Method 2: Caching global
fibonacci_cache = {}
def fibonacci_top_down(n):
  if n <= 2:
    return 1
  if n not in fibonacci_cache:
    fibonacci_cache[n] = fibonacci(n-1)+fibonacci(n-2)
  return fibonacci_cache[n]

# Method 3: Caching inside the function
def fibonacci(n):
  if n <= 2:
    return 1
  if not hasattr(fibonacci, 'cache'):
    fibonacci.cache = {}
  if n not in fibonacci.cache:
    fibonacci.cache[n] = fibonacci(n-1)+fibonacci(n-2)
  return fibonacci.cache[n]
print(fibonacci(6))

# Method 4: Better approach is to keep the original function simple and wrap it in a function with a decorator that performs caching
def cached(f):
  cache = {}
  def worker(*args):
    if args not in cache:
      cache[args] = f(*args)
    return cache[args]
  return worker

@cached
def fibonacci(n):
  if n<=2:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

# Method 5: Using python's inbuilt cache decorator lru_cache
from functools import lru_cache
@lru_cache(maxsize=None)
def fibonacci(n):
  if n<=2:
    return 1
  return fibonacci(n-1) + fibonacci(n-2)

# Bottom Up

def fibonacci(n):
  series = [1, 1]
  while len(series) < n:
    series.append(series[-1]+series[-2])
  return series[-1]

def fibonacci(n):
  previous = 1
  current = 1
  for i in range(n-2):
    next = current + previous
    previous, current = current, next
  return current

from numpy import matrix

def fib(n):
    return (matrix(
        '0 1; 1 1' if n >= 0 else '-1 1; 1 0', object
        ) ** abs(n))[0, 1]
        
def fib(n):
  if n < 0: return (-1)**(n % 2 + 1) * fib(-n)
  a = b = x = 1
  c = y = 0
  while n:
    if n % 2 == 0:
      (a, b, c) = (a * a + b * b,
                   a * b + b * c,
                   b * b + c * c)
      n /= 2
    else:
      (x, y) = (a * x + b * y,
                b * x + c * y)
      n -= 1
  return y