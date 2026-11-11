# B0610078 SALOHIDDIN USMONALIYEV

# TASK 1
# A small cinema wants a program that decides how much to charge 
# for a ticket, based on how old the customer is.

age = int(input("Enter your age: "))

if age <= 5:
    t_price = 0
elif 5<age<=17:
    t_price = 8
elif 18 <= age <= 64:
    t_price = 12
elif age >= 65:
    t_price = 9

print(f"Your ticket price: ${t_price}")


# TASK 2
# Write a program that checks whether a given number is prime or not.

num = int(input("Enter a number greatet than 1: "))
is_prime = True

for i in range(2, num):
    
    d = num%i

    if d==0:
        is_prime = False
        break

if is_prime:
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")


# TASK 3
# Printing simple shapes with loops is a classic exercise it helps 
# you see exactly how many times your loops are actually running.

h = int(input("Height: "))

for i in range(1, h+1):
    print("*"*i)

# TASK 4
# Write a program that the customer can take out money as 
# many times as they like, until they decide to stop.

balance = 500

while True:
    amount = int(input("Withdraw amount (0 to exit): "))

    if amount >= 0:
        if amount == 0:
            print("Thank you for using the ATM.")
            break
        elif balance >= amount:
            balance -= amount
            print(f"Withdraw: {amount}. Balance: {balance}")
        else:
            print("Insufficient funds.")
    else:
        print("Invalid number")


# TASK 5
# Write a program that a teacher has a list of student scores and wants the
# computer to grade each one automatically, and also count how many students passed.

count_students = int(input("How many students? "))
passed = 0
failed = 0

for i in range(1, count_students+1):
    score = int(input(f"Enter score {i}: "))

    if 0<=score<=100:
        if score > 60:
            passed += 1
        else:
            failed += 1

        if score>90:
            print("Grade: A")
        elif 80<=score<=89:
            print("Grade: B")
        elif 70<=score<=79:
            print("Grade: C")
        elif 60<=score<=69:
            print("Grade: D")
        else:
            print("Grade: F")

print(f"Total: {count_students}   Passed: {passed}   Failed: {failed}")