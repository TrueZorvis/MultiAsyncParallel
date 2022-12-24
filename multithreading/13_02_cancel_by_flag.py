import threading
import time
from multithreading.count_three_sum import read_ints

should_stop = False


def count_three_sum(ints, thread_name='t'):
    print(f'started count_three_sum in thread {thread_name}')

    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):

                if should_stop:
                    print('task was cancelled')
                    counter = -1
                    return counter

                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'Triple found in thread {thread_name}: {ints[i]}, {ints[j]}, {ints[k]}')
    print(f'ended count_three_sum in thread {thread_name}. triplets count: {counter}')
    return counter


if __name__ == '__main__':
    print('started main')

    ints = read_ints('..\\data\\1Kints.txt')
    t = threading.Thread(target=count_three_sum, args=(ints,))
    t.start()

    time.sleep(3)

    should_stop = True

    time.sleep(2)

    print('end main')



