"""
Замер времени выполнения параллельного вычисления против последовательного
"""
import threading
from count_three_sum import read_ints, count_three_sum
from decorators import measure_time


@measure_time
def run_in_parallel(ints1, ints2):
    t1 = threading.Thread(target=count_three_sum, daemon=True, args=(ints1, 't1'))
    t2 = threading.Thread(target=count_three_sum, daemon=True, args=(ints2, 't2'))

    t1.start()
    t2.start()

    print('\ngoing to wait for threads')

    t1.join()
    t2.join()


@measure_time
def run_sequentially(ints1, ints2):
    count_three_sum(ints1, 'main')
    count_three_sum(ints2, 'main')


if __name__ == '__main__':
    print('started main')

    ints1 = read_ints('..\\data\\1Kints.txt')
    ints2 = read_ints('..\\data\\2Kints.txt')

    run_in_parallel(ints1, ints2)
    run_sequentially(ints1, ints2)

    print('end main')
