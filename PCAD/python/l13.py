total = 0
price = int(input("Enter the price of the item: "))

while price != 0:
    total += price
    price = int(input("Enter the price of the item: "))

if total > 500:
    discount = total * 0.1
    total -= discount
else:
    discount = 0

print(f"Total: {total}, Discount: {discount}")
