# Implementing Multi-Processing
from multiprocessing import Process, Value, Array, Lock, Queue, Pool
import time

'''
def square_numbers():
    for x in range(100):
        print(x * x)
'''


def add_100(number, lock):
    for i in range(100):
        time.sleep(0.1)
        with lock:
            number.value += 1


def add_100_array(numbers_list, lock):
    for i in range(100):
        time.sleep(0.1)
        for x in range(len(numbers_list)):
            with lock:
                numbers_list[x] += 1


def square(numbers_list, queue):
    for i in numbers_list:
        queue.put(i * i)


def make_negative(numbers_list, queue):
    for i in numbers_list:
        queue.put(-1 * i)


def cube(number):
    return number * number * number


if __name__ == '__main__':
    '''
    processes = []

    # Number of CPUs on the machine.
    num_processes = os.cpu_count()

    # Create Process and assign the function to each process
    for i in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p)

    # Starting a Process
    for p in processes:
        p.start()

    # Wait for all the processes to finish and block the main program till these processes are done
    for p in processes:
        p.join()
    '''
    processLock = Lock()

    # Working with a shared Number
    shared_number = Value('i', 0)
    print("Number at beginning is ", shared_number.value)

    p1 = Process(target=add_100, args=(shared_number, processLock))
    p2 = Process(target=add_100, args=(shared_number, processLock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Number at end is ", shared_number.value)

    # Working with a shared array
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print("Array at the beginning ", shared_array[:])

    p1 = Process(target=add_100_array, args=(shared_array, processLock))
    p2 = Process(target=add_100_array, args=(shared_array, processLock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Array at the end is ", shared_array[:])

    # Working with a shared queue
    numbers = range(1, 6)
    q = Queue()

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())

    # Working with Process Pool
    pool = Pool()

    # Important Methods: map, apply, join, close
    numbers = range(10)

    result = pool.map(cube, numbers)
    # pool.apply(cube, numbers[0])

    pool.close()
    pool.join()

    print(result)
