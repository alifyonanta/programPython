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
