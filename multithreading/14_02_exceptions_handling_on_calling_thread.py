from concurrent.futures import ThreadPoolExecutor, CancelledError
import time


def div(divisor, limit):
    print(f'started div={divisor}')

    result = 0
    for x in range(1, limit):
        if x % divisor == 0:
            result += x
            print(f'divisor={divisor}, x={x}', end='\n')
        time.sleep(0.2)

    print(f'raise exception', end='\n')
    raise Exception("bad things happen!")

    return result


# Вариант обработки исключения в случае с map
if __name__ == '__main__':
    print('started main')

    with ThreadPoolExecutor(max_workers=2) as executor:
        res_list = executor.map(div, (3, 5), (15, 25))
        while res_list:
            try:
                cur_res = next(res_list)
            except StopIteration:
                print('stop iteration excepted')
                break
            except Exception as ex:
                print('generalized exception')
                print(repr(ex))

    print('ended main')


# Вариант обработки исключения в случае с submit
# if __name__ == '__main__':
#     print('started main')
#
#     with ThreadPoolExecutor(max_workers=1) as executor:
#         future = executor.submit(div, 3, 15)
#         time.sleep(5)
#
#         print('nothing happens until...')
#         try:
#             res = future.result()
#         except CancelledError as ex:
#             print(repr(ex))
#         except TimeoutError as ex:
#             print(repr(ex))
#         except Exception as ex:
#             print(repr(ex))
#
#     print('ended main')


