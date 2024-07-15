import threading
import time

read_count = 0
mutex = threading.Semaphore(1)
rw_mutex = threading.Semaphore(1)

def reader(reader_id):
    global read_count
    while True:
        # Reader entry section
        mutex.acquire()
        read_count += 1
        if read_count == 1:
            rw_mutex.acquire()
        mutex.release()

        # Reading (critical section)
        print(f"Reader {reader_id} is reading")
        time.sleep(1)  # Simulate the time taken to read

        # Reader exit section
        mutex.acquire()
        read_count -= 1
        if read_count == 0:
            rw_mutex.release()
        mutex.release()

        time.sleep(1)  # Simulate time before reading again

def writer(writer_id):
    while True:
        # Writer entry section
        rw_mutex.acquire()

        # Writing (critical section)
        print(f"Writer {writer_id} is writing")
        time.sleep(2)  # Simulate the time taken to write

        # Writer exit section
        rw_mutex.release()

        time.sleep(2)  # Simulate time before writing again

# Create reader and writer threads
reader_threads = []
writer_threads = []

for i in range(3):  # Create 3 readers
    t = threading.Thread(target=reader, args=(i,))
    reader_threads.append(t)

for i in range(2):  # Create 2 writers
    t = threading.Thread(target=writer, args=(i,))
    writer_threads.append(t)

# Start the threads
for t in reader_threads:
    t.start()

for t in writer_threads:
    t.start()

# Join the threads (optional, to keep the main thread waiting)
for t in reader_threads:
    t.join()

for t in writer_threads:
    t.join()
