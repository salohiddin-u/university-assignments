# B0610078 – SALOHIDDIN USMONALIYEV
# B0610052 – ABDULATIFXON AKBAROV
# B0610064 – MURODBEK ZIYADULLAYEV 
# V0610004 – BOZOROV BAHROM

import threading

numbers = [1, 2, 3,4, 5,6, 7, 8, 9,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

def sum_numbers_1():
    
    sum1 = 0
    for i in range(len(numbers) // 2):
        sum1 += numbers[i]
    print(f"Sum of the first half: {sum1}")

def sum_numbers_2():
    sum2 = 0
    for i in range(len(numbers) // 2, len(numbers)):
        sum2 += numbers[i]

    print(f"Sum of the second half: {sum2}")

# Creating threads
thread1 = threading.Thread(target=sum_numbers_1)
thread2 = threading.Thread(target=sum_numbers_2)

# Starting the threads
thread1.start()
thread2.start()

# Waiting for all threads to complete and combining the results
thread1.join()
thread2.join()