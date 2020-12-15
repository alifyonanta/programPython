#Functional Programming
def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))


#Lambdas
def my_func(f, arg):

  return f(arg)


my_func(lambda x: 2*x*x, 5)
#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))
double = lambda x: x * 2
print(double(7))

triple = lambda x: x * 3
add = lambda x, y: x + y
print(add(triple(3), 4))

#map
def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result1 = list(map(add_five, nums))
print(result1)

result2 = list(map(lambda x: x+5, nums))
print(result2)

#filter
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

#generator
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(20)))

#Decorators
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()

#Factorial
def factorial(x):
    if x == 1:
        return 1
    else: 
        return x * factorial(x-1)

print(factorial(5))

def fib(x):
  if x == 0 or x == 1:
    return 1
  else: 
    return fib(x-1) + fib(x-2)
print(fib(4))

#Sets
num_set = {1, 2, 3, 4, 5}
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second) # union operator
print(first & second) # intersection operator
print(first - second) # difference operator
print(second - first) # difference operator
print(first ^ second) # symmetric difference

#Decorators
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()

#intertools
from itertools import count

for i in count(3):
    print(i)
    if i >=11:
        break

from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))

from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(5))))
print(list(permutations(letters))) 
