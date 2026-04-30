import threading
import time

def worker(num):
    print(f"The thread {num}: started")
    time.sleep(2) # Simulate the work
    print(f"The thread {num}: Finished")

threads = [] # empty list
for i in range(3):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()  # Wait for all threads to finish

print("All threads completed")