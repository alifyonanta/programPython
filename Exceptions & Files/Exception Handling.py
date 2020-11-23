try:
    num1 = 7
    num2 = 8
    print (num1 / num2)
    print("Done calculation \n")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division\n")
    
#TRY yg kedua    
try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero\n")
except (ValueError, TypeError):
    print("Error occurred\n")    
    
#Finally
try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero\n")
finally:
    print("This code will run no matter what\n")
    
try:
    print(1)
    print(10 / 0)
except ZeroDivisionError:
    print(unknown_var)
finally:
    print("This is executed last\n")
    
#raise
name = "123"
raise NameError("Invalid name!\n")

#assert
print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)

temp = -10
assert (temp >= 0), "Colder than absolute zero!"

