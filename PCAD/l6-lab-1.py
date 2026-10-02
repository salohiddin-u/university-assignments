# B0610078 USMONALIYEV SALOHIDDIN

# TASK 1
name = input("Enter you name >")
fav_lang = input("What is you favorite programming language? ")

print(f"Your name: {name}, you favorite programming language: {fav_lang}")

# TASK 2
num_1 = float(input("Enter number 1: "))
num_2 = float(input("Enter number 2: "))

print(f"Sum: {num_1+num_2:.2f}")
print(f"Difference: {num_1-num_2:.2f}")
print(f"Product: {num_1*num_2:.2f}")
print(f"Quotient: {num_1/num_2:.2f}")

# TASK 3

morning_temp = float(input("Morning temperature (C): "))
afternoon_temp = float(input("Afternoon temperature (C): "))

morning_temp_in_f = (morning_temp*9/5)+32
afternoon_temp_in_f = (afternoon_temp*9/5)+32

morning_temp_in_k = morning_temp+273.15
afternoon_temp_in_k = afternoon_temp+273.15

average_c = (morning_temp+afternoon_temp)/2
average_f = (morning_temp_in_f+afternoon_temp_in_f)/2
average_k = (morning_temp_in_k+afternoon_temp_in_k)/2

print(f"{'':<10}{'C':>8}{'F':>8}{'K':>8}")
print(f"{'Morning':<10}{morning_temp:>8.2f}{morning_temp_in_f:>8.2f}{morning_temp_in_k:>8.2f}")
print(f"{'Afternoon':<10}{afternoon_temp:>8.2f}{afternoon_temp_in_f:>8.2f}{afternoon_temp_in_k:>8.2f}")
print(f"{'Average':<10}{average_c:>8.2f}{average_f:>8.2f}{average_k:>8.2f}")

# TASK 4

total_bill = float(input("Enter total bill: "))
tip_percent = int(input("Enter tip percentage: "))
people = int(input("How many people? "))

tip = total_bill*(tip_percent/100)

total = total_bill+tip

per_person = total/people

tip_l = f'Tip ({tip_percent}%):'

print("="*24)
print(f"{'Bill:':<13} {total_bill:>10.2f}")
print(f"{tip_l:<13} {tip:>10.2f}")
print(f"{'Grand total:':<13} {total:>10.2f}")
print(f"{'Per person:':<13} {per_person:>10.2f}")
print("="*24)

# TASK 5

q_score = int(input("Quiz score (0-100): "))
m_score = int(input("Midterm score (0-100): "))
f_score = int(input("Final score (0-100): "))

weighted = q_score*0.2+m_score*0.3+f_score*0.5

print(f"{'Quiz':<10}", q_score,"#"*(q_score//10))
print(f"{'Midterm':<10}", m_score, "#"*(m_score//10))
print(f"{'Final':<10}", f_score, "#"*(f_score//10))


print("-"*32)
print(f"{'Weighted':<10}", f"{weighted:.2f}", "#"*(int(weighted)//10))

