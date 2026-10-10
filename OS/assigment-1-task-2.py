# B0610078 – SALOHIDDIN USMONALIYEV
# B0610052 – ABDULATIFXON AKBAROV
# B0610064 – MURODBEK ZIYADULLAYEV 
# V0610004 – BOZOROV BAHROM

import threading

balance = 0

def deposit(amount):
    global balance
    balance += amount

    print(f"Deposited: {amount} | Balance: {balance}")

def withdraw(amount):

    global balance

    if balance >= amount:
        balance -= amount
        print(f"Withdrawn: {amount} | Balance: {balance}")
    else:
        print(f"Insufficient funds. Current balance: {balance}")

# Creating threads for deposit and withdraw
thread1 = threading.Thread(target=deposit, args=(100,))
thread2 = threading.Thread(target=withdraw, args=(50,))
thread3 = threading.Thread(target=deposit, args=(200,))
thread4 = threading.Thread(target=withdraw, args=(100,))

# Starting the threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()

# Waiting for all threads to complete and combining the results
thread1.join()
thread2.join()
thread3.join()
thread4.join()
