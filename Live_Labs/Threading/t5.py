import threading
import time
 
def task1():
    for i in range(3):
        print("Thread 1 running")
        time.sleep(2)   # pause for 2 second
 
def task2():
    for i in range(3):
        print("Thread 2 running")
        time.sleep(3)   # pause for 3 seconds
 
# Create two threads
t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
 
# Start threads
t1.start()
t2.start()
 
# Wait for both threads to complete
t1.join()
t2.join()
 
print("Main program finished")