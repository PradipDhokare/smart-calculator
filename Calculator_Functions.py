
import math
responses=["Hello. My name is Machine","What may I help you?","Thank You","Bye-Bye",
           "Sorry,I don't Know this","But Next time i will surely do"]

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y) //gcd(x, y)

# Area of Triangle (using base and height)
def area_triangle(base, height):
    return 0.5 * base * height

# Area of Circle (using radius)
def area_circle(radius):
    return 3.14 * radius * radius

# Area of Square (using side)
def area_square(side):
    return side * side

# Area of Rectangle (using length and width)
def area_rectangle(length, width):
    return length * width

import math

# Factorial Function
def factorial(n):
    if n < 0:
        return "Error: Negative number"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, int(n) + 1):
            result *= i
        return result

# Trigonometric Functions (use degrees)
def sin(x):
    return math.sin(math.radians(x))

def cosin(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))




def log_base_10(x):
    return math.log10(x)

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_even(n):
    return "Even" if n % 2 == 0 else "Odd"



def end():
    print(responses[2])
    print(responses[3])

def extract_num(t1):
    l1=[]
    for w in t1.split():
        try:
            l1.append(float(w))
        except:
            pass
    return l1

def amit():

    print("Amit is a student of xyz college")
    print("He is from Mumbai")

operations={"Addition":add,"SUM":add,"ADD":add,
            "SUB":sub,"SUBTRACT":sub,
            "MODULUS":modulus,
           "MINUS":sub,"MULTIPLY":mul,"PRODUCT":mul,"MULTIPLICTION":mul,
            "DIVISION":div,
            "GCD":gcd,"GREATEST COMMON DIVISOR":gcd,
            "LCM":lcm,"LEAST COMMON MULTIPLE":lcm,
            "LCF":gcd,"MCF":lcm,"LOWEST COMMON FACTOR":gcd,
            "MULTIPLE COMMON FACTOR":lcm,
            "AREA OF TRIANGLE":area_triangle,"AREA OF CIRCLE":area_circle,
            "POWER":power,
            "AREA OF SQUARE":area_square,
            "AREA OF RECTANGLE":area_rectangle,
            "FACTORIAL": factorial,"SIN": sin,
            "COSIN": cosin,"TAN": tan,
            "PRIME": is_prime,"EVEN": is_even,
            "LOG": log_base_10,
            "CELSIUS TO FAHRENHEIT": celsius_to_fahrenheit,
            "FAHRENHEIT TO CELSIUS": fahrenheit_to_celsius,
            "C TO F": celsius_to_fahrenheit,
            "F TO C": fahrenheit_to_celsius}

commands={"AMIT":amit,"BYE":end,"BYE-BYE":end,"EXIT":end}

    
