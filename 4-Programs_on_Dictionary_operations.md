## 1. Write a Python script to sort (ascending and descending) a dictionary by value
```py
my_dict = {'apple': 10, 'orange': 5, 'banana': 8, 'grape': 3}

sorted_dict_asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))

sorted_dict_desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

print("Sorted dictionary in ascending order:")
print(sorted_dict_asc)

print("\nSorted dictionary in descending order:")
print(sorted_dict_desc)
```
## 2. Write a Python Program to generate a temperature profile dictionary (values in range:30 to 100)for ten days randomly (from august 1 to august 31)  and check whether august 10 data exist in a dictionary or not. (Key=date,value=temperate value)
```py
import random
tempProf = {}
for i in range(11):    
    x = random.randrange(1,31)    
    y = random.randrange(30,100)    
    tempProf[x]=y
print("Day\t\t Temperature")
for day,temp in tempProf.items():    
    print("August ",day,"\t",temp)
flag = 10 in tempProf
if flag == False:    
    print("Does not exist")
else:    
    print('It exists')
```
## 3. In program 2, find the count of temperature 30,40 in the dictionary.
```py
import random
tempProf = {}
count1 = 0
count2 = 0

for i in range(11):    
    x = random.randrange(1,31)    
    y = random.randrange(30,100)    
    tempProf[x]=y
print("Day\t\t Temperature")
for day,temp in tempProf.items():    
    print("August ",day,"\t",temp)
for a in tempProf:    
    if tempProf[a] == 30:         
        count1+=1    
    if tempProf[a] == 40:        
        count2+=1
print('Count of temperature 30 in the temperature profile is: ',count1)
print('Count of temperature 40 in the temperature profile is: ',count2)
```
## 4. Repeat the program 2 for July month and write a python program to concatenate the two dictionaries into one dictionary named July_aug_temp.
```py
import random
from collections import defaultdict
tempProf_july = {}
tempProf_aug = {}
july_aug_temp = defaultdict(list)
for i in range(0,10):    
    x = random.randint(1,31)    
    y = random.randint(30,100)    
    s1="July "+str(x)    
    tempProf_july[s1]=y    
    m = random.randint(1,31)    
    n = random.randint(30,100)    
    s2="August "+str(m)    
    tempProf_aug[s2]=n
for tempProf in (tempProf_july, tempProf_aug):    
    for key, value in tempProf.items():        
        july_aug_temp[key].append(value)
print("Day\t\t Temperature")
for day,temp in july_aug_temp.items():    
    print(day," \t",temp[0])
```
## 5. Write a Python Program to multiply all the items in the dictionary “July_aug_temp”  which is generated in program 4 and find average temperate for the two months.
```py
import random
from collections import defaultdict
tempProf_july = {}
tempProf_aug = {}
july_aug_temp = defaultdict(list)
sumTemp = 0
count = 0
for i in range(0,10):    
    x = random.randint(1,31)    
    y = random.randint(30,100)    
    s1="July "+str(x)    
    tempProf_july[s1]=y    
    m = random.randint(1,31)    
    n = random.randint(30,100)    
    s2="August "+str(m)    
    tempProf_aug[s2]=n
for tempProf in (tempProf_july, tempProf_aug):    
    for key, value in tempProf.items():        
        july_aug_temp[key].append(value)
print("Day\t\t Temperature")
for day,temp in july_aug_temp.items():    
    print(day," \t",temp[0])
for days in july_aug_temp:    
    sumTemp+=july_aug_temp[days][0]    
    count+=1
avg=float(sumTemp)/count
print("The average temperature of july and august is %.2f"%avg)
```
# POST LAB QUESTIONS
## 1. Write a python program, that repeatedly asks the user to enter product names and prices. Store all of them in a dictionary whose keys are product names and values are prices. And also write a code to search an item from the dictionary.
```py
product_prices = {}

while True:
    product = input("Enter a product name (or 'q' to quit): ")
    if product == "q":
        break
    price = float(input("Enter the price of the product: "))
    product_prices[product] = price

print("Product prices:")
print(product_prices)

search_product = input("Enter a product name to search: ")
if search_product in product_prices:
    print(f"{search_product} costs {product_prices[search_product]:.2f}")
else:
    print(f"{search_product} is not in the product list.")
```
## 2. Write a Python program to get the maximum and minimum value in a dictionary.
```py
my_dict = {"a": 10, "b": 5, "c": 20, "d": 30}
max_value = max(my_dict.values())
min_value = min(my_dict.values())
print("Maximum value:", max_value)
print("Minimum value:", min_value)
```