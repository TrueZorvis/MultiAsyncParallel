from concurrent.futures import ThreadPoolExecutor
import time


def div(divisor, limit):
    print(f'started div={divisor}')

    for x in range(1, limit):
        if x % divisor == 0:
            print(f'divisor={divisor}, x={x}', end='\n')
        time.sleep(0.2)

    print(f'ended div={divisor}', end='\n')


if __name__ == '__main__':
    print('started main')

    # with ThreadPoolExecutor(max_workers=2) as executor:
    #     executor.submit(div, 3, 25)
    #     executor.submit(div, 5, 25)
    #     print('\nImmediately printed out after submit')
    # print('after with block')

    # Вариант без контекстного менеджера
    executor = ThreadPoolExecutor(max_workers=2)
    executor.submit(div, 3, 25)
    executor.submit(div, 5, 25)
    executor.shutdown(wait=True)

    print('\nend main')
