#!/usr/bin/env python3

def admin_login(username, password): ###def is a keyword (kuonyesha start of a function)
    ##then followed by a name of the function (parameters or arguments >>> this are placeholders for the values 
    ##  : >>> is used to indicate the start of a function body 
    ##Function body: The block of code that is executed when the function is called.
    # # It is indented under the def statement.
    if (username == "admin" or username == "ADMIN") and password == "12345":## the  bracket is used to group the
        ## equality comparisons and  comparison and clarify the order of evaluation 
        return "Access granted"
    else:
        return "Access denied" ##>>>> this returns is used to  specify the value that the function  should give 
        ##  when the function is called  the given out put is given and the input 
 
print(admin_login("admin", "12345"))   
print(admin_login("ADMIN", "12345"))    



def hows_the_weather(temperature): #### argument, a temperature
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

print(hows_the_weather(33)) 
print(hows_the_weather(75))    
print(hows_the_weather(99))    
     

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

print(fizzbuzz(1))     
print(fizzbuzz(2))     
print(fizzbuzz(3))      
print(fizzbuzz(4))     
print(fizzbuzz(5))     
print(fizzbuzz(15))    
  


def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None

print(calculator("+", 1, 1))  
print(calculator("/", 4, 2))    
print(calculator("-", 3, 1))    
print(calculator("*", 3, 2))    
print(calculator("nope", 4, 2))  
