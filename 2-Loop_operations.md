## 1. Write a function that returns the maximum of two numbers. (Use if loop)
```py
num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
def max(num1, num2):
    if(num1 > num2):
        print(f"The Maximum Number is : {num1}")
    else:
        print(f"The Maximum Number is : {num2}")

max(num1,num2)
```
## 2. Write a function called divisible that takes a number. ( Use if loop)  
## If the number is divisible by 3, it should return “Three”. 
## If it is divisible by 5, it should return “Five”. 
## If it is divisible by both 3 and 5, it should return “Three and Five”
```py
num = int(input("Enter a Number : "))

def divisible(num):
    if(num%3 == 0 and num%5 == 0):
        print("Three and Five")
    elif(num%3 == 0):
        print("Three")
    else:
        print("Five")

divisible(num)
```
## 3. Write a function for checking the speed of drivers. This function should have one parameter: speed.
## a) If speed is less than 70, it should print “Ok”.
## b) Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
## c) If the driver gets more than 12 points, the function should print: “License suspended”
```py
speed = int(input("Enter the Speed"))

def speed_of_drivers(speed):
    point = int((speed-70)/5)
    if(speed <= 70):
        print("OK")
    elif(speed > 70 and point < 12):
        print(f"Points : {point}")
    else:
        print("License Suspended")

speed_of_drivers(speed)
```
## 4. Write a function(Use for loop) called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:
```py
limit = int(input("Enter the Number: "))
def shownumbers(limit):
    for x in range(limit+1):
        if x%2 == 0:
            print(f"{x} EVEN")
        else:
            print(f"{x} ODD")
        
shownumbers(limit)
```
## 5. Write a program using while loop to check the number n is less than seven. If it is less than seven, print n is less than 7 and add 1 to n. If it is greater than 7,  print n is not less than 7.
```py
num = int(input("Enter the Number : "))
while(num <= 7):
    if num < 7:
        print(f"{num} is less than 7")
    else:
        print(f"{num} is Equal to 7")
    num += 1

print(f"{num} is not less than 7")
```

# POST LAB QUESTIONS
## 1. Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
```py
limit = int(input("Enter the Limit : "))

for num in range(limit):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
```
## 2 .Write a Python program to find a Factorial of a Number using Loop
```py
num = int(input("Enter the Number : "))
factorial = 1
if num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
```