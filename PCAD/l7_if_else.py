score = int(input("Enter you score >>> "))

if 0<=score<=100:
    if score>90:
        print("A")
    elif 89>=score>=80:
        print("B")
    elif 70<=score<=79:
        print("C")
    elif 60<=score<=69:
        print("D")
    else:
        print("F")