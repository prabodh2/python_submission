import threading
import time

def print_hello():
    for _ in range(5):
        time.sleep(1)  # Simulate some work
        print("Hello")

def print_hi():
    for _ in range(5):
        time.sleep(1)  # Simulate some work
        print("Hi")

# Create threads
thread_hello = threading.Thread(target=print_hello)
thread_hi = threading.Thread(target=print_hi)

# Start threads
thread_hello.start()
thread_hi.start()

# Wait for threads to finish
thread_hello.join()
thread_hi.join()

