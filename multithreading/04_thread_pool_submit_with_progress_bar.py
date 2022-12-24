from concurrent.futures import ThreadPoolExecutor
import time


def div(divisor, limit):
    print(f'started div={divisor}')

    result = 0
    for x in range(1, limit):
        if x % divisor == 0:
            result += x
        time.sleep(0.2)

    print(f'\nended div={divisor}', end='\n')
    return result


if __name__ == '__main__':
    print('started main')

    futures = []
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures.append(executor.submit(div, 3, 25))
        futures.append(executor.submit(div, 5, 25))

        while futures[0].running() and futures[1].running():
            print('.', end='')
            time.sleep(0.5)

        for f in futures:
            print(f.result())  # блокирующий вызов

    print('\nend main')
