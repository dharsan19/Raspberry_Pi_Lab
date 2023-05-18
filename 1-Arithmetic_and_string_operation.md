## 1. Write a  Python program to perform arithmetic operations on two integers.
```py
def perform_arithmetic_operations(a, b):
    print("Addition: ", a + b)
    print("Subtraction: ", a - b)
    print("Multiplication: ", a * b)
    print("Division: ", a / b)
    print("Modulo: ", a % b)
    print("Exponentiation: ", a ** b)

num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

perform_arithmetic_operations(num1, num2)
```
## 2. Write a Python Program to find area of a triangle.
```py
def calculate_triangle_area(base, height):
    area = 0.5 * base * height
    return area

base = float(input("Enter the base length of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = calculate_triangle_area(base, height)

print("The area of the triangle is: ", area)
```
## 3. Write a Python code to remove 6 characters from start of given string “Embedded Systems”
```py
string = "Embedded Systems"

new_string = string[6:]

print(new_string)
```
## 4. Write the Python code to find length of String “Computer Science”. Replace science with Electronics.
```py
string = "Computer Science"

length = len(string)

new_string = string.replace("Science", "Electronics")

print("Length of the string:", length)
print("New string:", new_string)
```
## 5. Write the Python program to reverse a string from user input
```py
string = input("Enter a string: ")

reversed_string = string[::-1]

print("Reversed string:", reversed_string)
```
# PRE LAB QUESTIONS
## 2. Convert all the characters in the string “Raspberry” to upper case using python code.
```py
string = "Raspberry"

uppercase_string = string.upper()

print(uppercase_string)
```
# POST LAB QUESTIONS
## 1.Write Python program to find area of a circle.
```py
import math

def calculate_circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

radius = float(input("Enter the radius of the circle: "))

area = calculate_circle_area(radius)

print("The area of the circle is:", area)
```