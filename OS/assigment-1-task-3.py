# B0610078 – SALOHIDDIN USMONALIYEV
# B0610052 – ABDULATIFXON AKBAROV
# B0610064 – MURODBEK ZIYADULLAYEV 
# V0610004 – BOZOROV BAHROM

import threading 
import time

def submit(name):

    print(f"{name} is trying to submit the assignment at 23:59")

    print(f"{name} started uploading...")
    time.sleep(2)

    print(f"{name} successfully submitted!")

# Creating threads for each student
thread1 = threading.Thread(target=submit, args=("Student 1",))
thread2 = threading.Thread(target=submit, args=("Student 2",))
thread3 = threading.Thread(target=submit, args=("Student 3",))
thread4 = threading.Thread(target=submit, args=("Student 4",))
thread5 = threading.Thread(target=submit, args=("Student 5",))
thread6 = threading.Thread(target=submit, args=("Student 6",))

# Starting the threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()

# Waiting for all threads to complete and combining the results
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()




