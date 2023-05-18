## 1. Write a python program to interchange first and last elements in a list.
```py
list1 = ["Zero","One","Two","Three","Four","Five"]
def interchange(list1):
    temp = ""
    temp = list1[0]
    list1[0] = list1[-1]
    list1[-1] = temp
    print(list1[0:])
interchange(list1)
```
## 2. Write a Python program to find N largest and smallest elements from the list
```py
list2 = [1,2,3,4,5,6,7,8,9,10]
list2.sort(reverse=True)
def largeandsmall(list2):
    n = int(input("Enter the Value of N :"))
    print("The N Largest Elements from the list : ")
    print(list2[:n])
    print("The N smallest Elements from the list : ")
    print(list2[-n:])
largeandsmall(list2)
```
## 3. Write a python program to find the cumulative sum of elements in a list
```py
list3  = [1,2,3,4,5,6,7,8,9,10]
def cummulative(list3):
    list3a = list()
    sum = 0
    for a in list3:
        sum += a
        list3a.append(sum)
    print(list3a)
cummulative(list3)
```
## 4. Write a python program to find positive numbers from a list.
```py
list4 = [-1,-3,-4,4,5,-9,10]
def positive(list4):
    for a in list4:
        if a > 0:
            print(a, end = " ")
positive(list4)
```
## 5. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
```py
def values():
    list5 = list()
    for a in range(1,30):
        list5.append(a**2)
    print(list5[:5])
    print(list5[-5:])
values()
```
# POST LAB QUESTIONS
## 1. Write a Python | Program to create two lists with EVEN numbers and ODD numbers from a list
```py
list1 = [1, 2, 3, 4, 5]
listOdd = []
listEven = []
for num in list1:
	if num%2 == 0:
		listEven.append(num)
	else:
		listOdd.append(num) 
print("list1:    ", list1 )
print("listEven: ", listEven)
print("listOdd:  ", listOdd)
```
## 2. Write a Python program to multiply all numbers of a list
```py
def multiplyList(myList):
    result = 1
    for x in myList:
        result = result * x
    return result

list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))
```