# B0610078 SALOHIDDIN USMONALIYEV
# LAB 3

# TASK 1 - A weather station wants to log daily temperature readings and report some Simple statistics.
number_of_temp = int(input("Enter the number of temperature readings: "))
temperature_readings = []
for i in range(number_of_temp):
    temp = float(input(f"Enter temperature reading {i + 1}: "))
    temperature_readings.append(temp)

print("Temperature readings:", temperature_readings)
print("Number of readings:", len(temperature_readings))
print(f"Maximum {max(temperature_readings):>5} Minimum {min(temperature_readings):>5} Average {sum(temperature_readings)/len(temperature_readings):>5.2f}")


# TASK 2 - A teacher keeps a simple list of student names and wants to quickly check whether a student is enrolled.
number_of_students = int(input("Enter the number of students: "))
students = []
for i in range(number_of_students):
    name = input(f"Enter name of student {i + 1}: ")
    students.append(name)

search_name = input("Enter the name of the student to search for: ")
if search_name in students:
    print(f"{search_name} found at position {students.index(search_name)+1}.")
else:
    print(f"{search_name} is not in the list.")


# TASK 3 - A classroom's reserved seats are modeled as a 2D list, where each inner list is one row and each number is how many students are sitting in that seat group.
seating = [[2, 3, 1], [0, 4, 2], [3, 3, 3]]
total = 0
for row in enumerate(seating):
    total += sum(row[1])
    print(f"Row {row[0]+1}: ", sum(row[1]))

print("Total students: ", total)


# TASK 4 - You are building a small phone book that looks up a number by a person's name.
number_of_contacts = int(input("Enter the number of contacts: "))
phone_book = {}
for i in range(number_of_contacts):
    name = input(f"Enter name of contact {i + 1}: ")
    number = input(f"Enter phone number of contact {i + 1}: ")
    phone_book[name] = number

search_name = input("Enter the name of the contact to search for: ")
if phone_book.get(search_name):
    print(f"{search_name}: {phone_book[search_name]}")
else:
    print("Contact not found.")

# TASK 5 - A small store wants to track stock levels and let a cashier sell items until they are done for the day.
inventory = {"pen": 40, "notebook": 25, "eraser": 15}

while True:
    product = input("Enter product name (or 'done' to finish): ")
    if product == 'done':
        break
    if product in inventory:
        qty = int(input("Sold: "))
        if qty<=inventory[product]:
            inventory[product] -= qty
        else:
            print("Not enough")

    else:
        print("No such product.")

for item, qty in inventory.items():
    print(f"{item}: {qty}")