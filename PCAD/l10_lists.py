r = int(input("How many students? "))

attendace = []

for i in range(r):
    name = input(f"Enter student {i} name: ")
    attendace.append(name)

while True:
    student = input("Enter student's name to check attendace: ")
    if student==0:
        break
    if student in attendace:
        print(f"{student} is present")
    else:
        print(f"{student} is absent")
    