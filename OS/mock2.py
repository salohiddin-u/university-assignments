# MULTITHREADING IN PYTHON
# TASK 1
import threading

def print_numbers():
    for i in range(1, 11):
        print(i)


t1 = threading.Thread(target=print_numbers)
t1.start()

# TASK 2
numbers = [i for i in range(1, 21)]

def odd_nums():
    for i in numbers:
        if i%2:
            print(i)

def even_nums():
    for i in numbers:
        if not i%2:
            print(i)

th1 = threading.Thread(target=odd_nums)
th2 = threading.Thread(target=even_nums)

th1.start()
th2.start()

th1.join()
th2.join()
