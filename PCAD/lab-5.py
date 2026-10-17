# B0610078 SALOHIDDIN USMONALIYEV
# LAB 5

# TASK 1
"""
The university wants a small program that keeps information about a student. 
Instead of several separate variables, you will describe a student with a class.
"""

# class Student:
#     def __init__(self, name, group):
#         self.name = name
#         self.group = group
#         self.grades = []

#     def add_grade(self, grade):
#         self.grades.append(grade)

#     def average(self):
#         if len(self.grades) == 0:
#             return 0
#         return sum(self.grades) / len(self.grades)

#     def __str__(self):
#         return f"{self.name} ({self.group}): {self.average():.1f}"


# student = Student("Aziz", "CSE-11")
# student.add_grade(80)
# student.add_grade(90)
# student.add_grade(100)

# print(student)



# TASK 2

"""
A bank wants to model its accounts. 
Every account belongs to one owner and has its own balance, so two accounts must not affect each other.
"""

# class Account:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Not enough money")
#         else:
#             self.balance -= amount

#     def __str__(self):
#         return f"{self.owner}: {self.balance}"

# owner1 = Account("Dilnoza", 50000)
# owner2 = Account("Timur")

# owner1.deposit(20000)
# owner1.withdraw(100000)
# owner1.withdraw(30000)
# owner2.deposit(10000)

# print(owner1)
# print(owner2)



# Task 3
"""
A small shop stores each product as an object. You will create several objects, 
keep them in a list and work with them in a loop.

"""


# class Product:
#     def __init__(self, name, quantity, price):
#         self.name = name
#         self.quantity = quantity
#         self.price = price

#     def total(self):
#         return self.quantity * self.price

#     def __str__(self):
#         return f"{self.name} x{self.quantity} = {self.total()}"



# products = [Product("Pen", 3000, 10), Product("Notebook", 12000, 5), Product("Bag", 150000, 1)]

# total = 0
# for product in products:
#     print(product)
#     total += product.total()
# print(f"Total: {total}")



# TASK 4
"""
A weather station keeps temperatures in Celsius in a list. 
The station needs the same data in Fahrenheit and a list of only the hot days. 
The original list must stay unchanged.
"""

# temps = [22, 31, 18, 35, 27]

# fahrenheit = list(map(lambda c: c * 9 / 5 + 32, temps))
# hot_days = list(filter(lambda c: c > 25, temps))

# print(temps)
# print(fahrenheit)
# print(hot_days)
# words = ["python", "is", "fun"]
# word_lengths = list(map(len, words))
# print(word_lengths)





# TASK 5

"""
An online shop keeps the cart as a tuple, because a tuple cannot be changed by accident. You will write pure functions that never change their input and always return a new result.
"""

cart = ("milk", "bread")

def add_item(cart, item):
    return cart + (item,)

def average(numbers):
    return sum(numbers) / len(numbers)
new_cart = add_item(cart, "eggs")
print(cart, new_cart)
print(average([22, 31, 18, 35, 27]))

# it is pure function because it doesn't change the original cart ('milk', 'bread') and return a new cart ('milk', 'bread', 'eggs')