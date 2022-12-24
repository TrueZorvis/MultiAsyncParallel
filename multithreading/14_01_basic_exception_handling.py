import threading
import time

throw = False


def count():
    i = 0
    try:
        while True:
            if throw:
                raise ZeroDivisionError()

            i += 1
            print(f'{i=}')
            time.sleep(1)
    except ZeroDivisionError:
        print('exception occurred')


if __name__ == '__main__':
    print('started main')

    t = threading.Thread(target=count)
    t.start()

    time.sleep(3)

    throw = True

    for x in range(1, 5):
        print(f'{x=}')
        time.sleep(1)

    print('ended main')
