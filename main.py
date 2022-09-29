import threading
import time

# def counter():
#     for i in range(100):
#         print(f"Thread: {i}")

# x = threading.Thread(target=counter)

# print(threading.active_count())
# x.start()
# print(threading.active_count())

#############################################################################

# def counter1(nome):
#     for x in range(100):
#         print(f"{nome} count: {x}")

# thread1 = threading.Thread(target=counter1, args=('Thread-1',))
# thread2 = threading.Thread(target=counter1, args=('Thread-2',))

# thread1.start()
# thread1.join()
# thread2.start()

#############################################################################

# x = 8192

# lock = threading.Lock()

# def double():
#     global x, lock
#     lock.acquire()
#     while x < 16384:
#         x *= 2
#         print(x)
#         time.sleep(1)
#     print(f"Reached the maximum!")
#     lock.release()

# def halve():
#     global x, lock
#     lock.acquire()
#     while x > 1:
#         x /= 2
#         print(x)
#         time.sleep(1)
#     print(f"Reached the minimum!")
#     lock.release()

# t1 = threading.Thread(target=halve)
# t2 = threading.Thread(target=double)

# t1.start()
# t2.start()

#############################################################################

# semaphore = threading.BoundedSemaphore(value=5)

# def access(thread_number):
#     print(f"{thread_number} is trying to access!")
#     semaphore.acquire()
#     print(f"{thread_number} was granted access!")
#     time.sleep(10)
#     print(f"{thread_number} is now releasing...")
#     semaphore.release()

# for thread_number in range(1, 11):
#     t = threading.Thread(target=access, args=(thread_number,))
#     t.start()
#     time.sleep(1)

#############################################################################

path = "text.txt"
text = ""

exit_event = threading.Event()

def readFile():
    global path, text
    while True:
        with open(path, "r") as f:
            text = f.read()
        time.sleep(3)

        if exit_event.is_set():
            break

    print(f"Terminating the reading process...")


def printLoop():
    for x in range(30):
        print(text)
        time.sleep(1)


t1 = threading.Thread(target=readFile)
t2 = threading.Thread(target=printLoop)
t1.start()
t2.start()

time.sleep(4)
exit_event.set()