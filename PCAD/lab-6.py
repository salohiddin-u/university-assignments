# SALOHIDDIN USMONALIYEV 
# B0610078
# LAB ASSIGMENT 6

"""
TASK 1
A pet shop keeps information about its animals. All animals have a name and
can speak, but every kind of animal speaks in its own way. Use inheritance, so you
do not repeat the same code
"""

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def speak(self):
        print(f"{self.name} says Woof!")
    def info(self):
        print(f"{self.name} is a {self.breed}.")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def speak(self):
        print(f"{self.name} says Meow!")

animals = [Animal("Generic"), Dog("Rex", "husky"), Cat("Tom")]

for animal in animals:
    animal.speak()

Dog("Rex", "husky").info()


"""
TASK 2
A small library keeps books and DVDs. Both are items with a title, but a book
also has an author and a DVD has a length in minutes. Build the classes with
inheritance.
"""

class Item:
    def __init__(self, title):
        self.title = title
    def info(self):
        print(f"Item: {self.title}")

class Book(Item):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author
    def info(self):
        print(f"Book: {self.title} by {self.author}")

class DVD(Item):
    def __init__(self, title, minutes):
        super().__init__(title)
        self.minutes = minutes

    def info(self):
        print(f"DVD: {self.title}, {self.minutes} min")

items = [
    Item("Map"), Book("Python 101", "Ali"), DVD("matrix", 136)
]
obj = 0
for item in items:
    item.info()
    if isinstance(item, Item):
            obj += 1

print(f"Total items: {len(items)}")
print(f"Objects that are Item: {obj}")


"""
TASK 3
A bank has ordinary accounts and savings accounts. A savings account works
like an ordinary account, but it also pays interest. Extend the existing class, do not
copy it.
"""

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough money")

    def __str__(self):
        return f"{self.owner}: {self.balance}"


class SavingsAccount(Account):
    def __init__(self, owner, balance, rate):
        super().__init__(owner, balance)
        self.rate = rate

    def add_interest(self):
        self.balance += self.balance * self.rate/100

    def __str__(self):
        super().__str__()
        return f"{self.owner}: {self.balance}  (savings, {self.rate}%)"

account = SavingsAccount("Dilnoza", 1000, 10)
account.deposit(500)
account.add_interest()
account.withdraw(5000)
print(account)