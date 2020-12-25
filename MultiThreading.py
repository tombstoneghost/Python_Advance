# Implementing MultiThreading
from threading import Thread, Lock, current_thread
import time
from queue import Queue


'''
def square_numbers():
    for x in range(100):
        x * x
'''

database_value = 0


def increase(lock):
    global database_value

    with lock:
        local_copy = database_value

        # Processing
        local_copy += 1
        time.sleep(0.1)

        database_value = local_copy


def worker(queue, lock):
    while True:
        value = queue.get()

        # Processing
        with lock:
            print(f"in {current_thread().name} got {value}")
        queue.task_done()


if __name__ == '__main__':
    '''
    threads = []
    num_threads = 10

    # Create Thread
    for i in range(num_threads):
        t = Thread(target=square_numbers)
        threads.append(t)

    # Starting a Thread
    for t in threads:
        t.start()

    # For Joining the Thread with the main thread
    for t in threads:
        t.join()

    print("End Main")
    '''

    threadLock = Lock()

    print("Start Value", database_value)

    thread1 = Thread(target=increase, args=(threadLock,))
    thread2 = Thread(target=increase, args=(threadLock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('End Value', database_value)

    q = Queue()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, threadLock))
        # Comment out the below line to get a synchronized result.
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()
