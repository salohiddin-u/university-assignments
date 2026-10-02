name = input("Name >>> ")
age = int(input("Age >>> "))
height = float(input("Height >>> "))

print(f'{"Name":<10}',f'{"Age":<10}',f'{"Height"}', sep="|")
print(f"{name:<10}{age:<10}{height:.2f}", end="cm")
