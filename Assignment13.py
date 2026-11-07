
import threading
import time

# Task 1
def task1():
    for i in range(1, 4):
        print("Task 1: Printing", i)
        time.sleep(1)

# Task 2
def task2():
    for i in range(1, 4):
        print("Task 2: Squaring", i, "=", i * i)
        time.sleep(1)

# Task 3
def task3():
    for i in range(1, 4):
        print("Task 3: Cubing", i, "=", i * i * i)
        time.sleep(1)

# Create threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)

# Start threads
t1.start()
t2.start()
t3.start()

# Wait for all threads to finish
t1.join()
t2.join()
t3.join()

print("All tasks completed!")