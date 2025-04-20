# deadlock_example.py

import threading
import time

# Create two shared resources (locks)
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    print("Thread 1: Trying to acquire Lock 1...")
    lock1.acquire()
    print("Thread 1: Acquired Lock 1")
    time.sleep(1)
    print("Thread 1: Trying to acquire Lock 2...")
    lock2.acquire()
    print("Thread 1: Acquired Lock 2")

    # Simulating work
    print("Thread 1: Working in critical section")
    lock2.release()
    lock1.release()

def thread2():
    print("Thread 2: Trying to acquire Lock 2...")
    lock2.acquire()
    print("Thread 2: Acquired Lock 2")
    time.sleep(1)
    print("Thread 2: Trying to acquire Lock 1...")
    lock1.acquire()
    print("Thread 2: Acquired Lock 1")

    # Simulating work
    print("Thread 2: Working in critical section")
    lock1.release()
    lock2.release()

# Create threads
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

# Start threads
t1.start()
t2.start()

# Wait for threads to complete
t1.join()
t2.join()

# PS D:\ReactExpo\dc> py deadlock.py
#Thread 1: Trying to acquire Lock 1...
#Thread 1: Acquired Lock 1
#Thread 2: Trying to acquire Lock 2...
#Thread 2: Acquired Lock 2
#Thread 1: Trying to acquire Lock 2...
#Thread 2: Trying to acquire Lock 1...