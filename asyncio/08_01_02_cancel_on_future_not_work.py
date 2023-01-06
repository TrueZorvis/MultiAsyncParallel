import asyncio


class ErrorThatShouldCancelOtherTasks(Exception):
    pass


async def my_sleep(secs):
    print(f'task {secs}')
    await asyncio.sleep(secs)
    print(f'task {secs} finished sleeping')

    if secs == 5:
        raise ErrorThatShouldCancelOtherTasks('5 is forbidden')

    print(f'slept for {secs} seconds')


# Такая отмена не убивает таск (таск 7 будет работать)
async def main_cancel_future():
    sleepers = asyncio.gather(*[my_sleep(secs) for secs in [2, 5, 7]])
    print('awaiting')
    try:
        await sleepers
    except ErrorThatShouldCancelOtherTasks:
        print('fatal error. cancelling...')
        sleepers.cancel()
    finally:
        await asyncio.sleep(5)


# Такая отмена тасков работает
async def main_cancel_tasks():
    tasks = [asyncio.create_task(my_sleep(secs)) for secs in [2, 5, 7]]
    sleepers = asyncio.gather(*tasks)
    print('awaiting')
    try:
        await sleepers
    except ErrorThatShouldCancelOtherTasks:
        print('fatal error. cancelling...')
        for t in tasks:
            print(f'cancelling {t}')
            res = t.cancel()
            print(f'cancelling result: {res}')
    finally:
        await asyncio.sleep(5)


if __name__ == '__main__':
    # asyncio.run(main_cancel_future())
    asyncio.run(main_cancel_tasks())
