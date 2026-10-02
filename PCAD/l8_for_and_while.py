num = int(input("Enter number: "))

while True:
    print(num)

    num -= 1
    if num == 0:
        print("Litoff!")
        a = input("Do you want to continue? ")
        if a == "yes":
            num = int(input("Enter number: "))
        elif a == "no":
            break
    elif num<0:
        print("Invalid number")
        num = int(input("Enter number: "))
        