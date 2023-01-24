import math

a = int(input("Enter the first Side : "))
b = int(input("Enter the Second Side : "))
c = int(input("Enter the Third Side : "))
s = (a + b + c)/2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(f"The Area of the Triangle : {area}")
