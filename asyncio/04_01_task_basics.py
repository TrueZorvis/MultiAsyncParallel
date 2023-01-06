import asyncio


async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')
    return 'Tick-Tock'


async def main():
    t1 = asyncio.create_task(tick(), name='task 1')
    t2 = asyncio.ensure_future(tick())

    # result1 = await t1
    # result2 = await t2
    # print(result1)
    # print(result2)

    # Вместо вызовов await если тасков много
    results = await asyncio.gather(t1, t2)
    for res in results:
        print(res)

    print(f'{t1.get_name()}. Done = {t1.done()}')
    print(f'{t2.get_name()}. Done = {t2.done()}')


if __name__ == '__main__':
    asyncio.run(main())
