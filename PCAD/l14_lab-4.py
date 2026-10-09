"""
B0610078 - SALOHIDDIN USMONALIYEV 
LAB 4
"""
# TASK 1 - A cafe prints the same welcome message on every table card and does not want to repeat code.
def print_banner():
    print("Welcome to Cafe Aroma!")
    print("Special: green tea")
    print("---")

print("Table 1")
print_banner()

print("Table 2")
print_banner()

print("Table 3")
print_banner()

def print_banner_for(name):
    print(f"Welcome, {name}!")
    print_banner()

print_banner_for("Ali")
print_banner_for("Vali")


# TASK 2 - A restaurant wants a helper that calculates the tip for a bill. 
# Most customers tip 10%, but some choose a different percentage.
def calculate_tip(bill, percent=10):
    return (bill * percent / 100)

def print_receipt(bill, tip):
    print(f"Bill: {bill}   Tip: {tip:.1f}   Total: {bill + tip:.1f}")

bill = int(input("Enter the bill amount: "))
tip = calculate_tip(bill)
print_receipt(bill, tip)
tip = calculate_tip(bill, 15)
print_receipt(bill, tip)


# TASK 3 - A courier company charges a base fee plus a price per kilogram, and doubles 
# the cost for express delivery.
def delivery_cost(weight_kg, express=False):
    cost = 10000 + (2000 * weight_kg)
    if express:
        cost *= 2
    return cost

def is_heavy(weight_kg):
    if weight_kg > 20:
        return True
    return False

weight = int(input("Enter the weight of the package: "))
is_express = input("Is it express delivery? (yes/no): ").lower()
if is_express == "yes":
    express = True
else:
    express = False

cost = delivery_cost(weight, express)
if is_heavy(weight):
    print(f"The package is heavy.")
print(f"Delivery cost: {cost} so'm")


# TASK 4 - A university website wants to accept only strong passwords. A password is 
# strong if it has at least 8 characters AND contains at least one digit.

"""
DECOMPOSITION
Problem: university website wants to accept only stong passwords. A password is strong if it has at least 8 characters AND contains at least one digit.
Sub-problem 1: Get the password from the user
Sub-problem 2: Check if the password has at least 8 characters
Sub-problem 3: Check if the password contains at least one digit
Sub-problem 4: If both conditions are met, print "Password accepted"
"""
def has_digit(password):
    for i in password:
        if i.isdigit():
            return True
    return False

def is_strong(password):
    if len(password) >= 8 and has_digit(password):
        return True
    return False

while True:
    password = input("Enter your password: ")
    if is_strong(password):
        print("Password accepted")
        break
    else:
        print("Weak password. Please try again.")

# TASK - 5 Build a complete small program for a cafe from several functions, in the same 
# way as the example from the lecture. The menu is stored in a dictionary and the 
# customer order in a list.
menu = {"tea": 12000, "coffee": 18000, "cake": 25000}
order = ["coffee", "cake", "cake", "tea"]

def show_menu(menu):
    for name, price in menu.items():
        print(f"{name} - {price}")

def calculate_total(menu, order):
    total = 0
    for item in order:
        total += menu.get(item, 0)
    return total

def apply_discount(total, percent=10):
    if total > 50000:
        discount = total * percent / 100
        return total - discount
    return total

def print_bill(total, final):
    print("Total: ", total)
    print("Total after discount: ", final)

show_menu(menu)

total = calculate_total(menu, order)
final = apply_discount(total)
print_bill(total, final)