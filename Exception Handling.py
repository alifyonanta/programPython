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
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred")    
