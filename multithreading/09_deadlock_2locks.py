import threading
import time

a = 5
b = 5

a_lock = threading.Lock()
b_lock = threading.Lock()


def thread1calc():
    global a
    global b

    print('thread1 acquiring lock a\n')
    a_lock.acquire()
    time.sleep(5)

    print('thread1 acquiring lock b\n')
    b_lock.acquire()
    time.sleep(5)

    a += 5
    b += 5

    print('thread1 releasing both locks\n')
    a_lock.release()
    b_lock.release()


def thread2calc():
    global a
    global b

    print('thread2 acquiring lock b\n')
    b_lock.acquire()
    time.sleep(5)

    print('thread2 acquiring lock a\n')
    a_lock.acquire()
    time.sleep(5)

    a += 10
    b += 10

    print('thread2 releasing both locks\n')
    b_lock.release()
    a_lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=thread1calc)
    t2 = threading.Thread(target=thread2calc)

    t1.start()
    t2.start()
