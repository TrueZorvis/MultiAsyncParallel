from concurrent.futures import ThreadPoolExecutor
from count_three_sum import count_three_sum, read_ints


if __name__ == '__main__':
    print('started main')

    data1 = read_ints('..\\data\\1Kints.txt')
    data2 = read_ints('..\\data\\2Kints.txt')

    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(count_three_sum, (data1, data2), ('t1', 't2'))
        print('\nafter map')
        for r in results:
            print(f'result: {r}')  # блокирующий вызов
        print('\nafter for')

    print('\nend main')
