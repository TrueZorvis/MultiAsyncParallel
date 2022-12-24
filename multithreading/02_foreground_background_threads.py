"""
Решение проблемы
"""
import threading
from count_three_sum import read_ints, count_three_sum


if __name__ == '__main__':
    print('started main')

    ints = read_ints('..\\data\\1Kints.txt')

    # t1 = threading.Thread(target=count_three_sum, daemon=True, args=(ints,))  # передача одного аргумента
    t1 = threading.Thread(target=count_three_sum, daemon=True, kwargs=dict(ints=ints))  # передача именованных аргументов
    t1.start()

    print(input('\nwhat is your name?'))

    t1.join()
    print('end main')
