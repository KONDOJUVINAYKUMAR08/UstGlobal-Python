import threading

count=0

def task():
    global count
    for _ in range(1000):
        count += 1

t1 = threading.Thread(target=task())
t2 = threading.Thread(target=task())

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Count:",count)