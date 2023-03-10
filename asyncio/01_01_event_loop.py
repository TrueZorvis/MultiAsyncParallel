import asyncio


async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')

    loop = asyncio.get_running_loop()
    if loop.is_running():
        print('loop is still running')


async def main():
    awaitable_object = asyncio.gather(tick(), tick(), tick())

    for task in asyncio.all_tasks():
        print(task, end='\n')

    await awaitable_object


if __name__ == '__main__':
    # asyncio.run(main())

    # Примерный разворот функции asyncio.run(main())
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
        print('coroutines have finished')
    finally:
        loop.close()
        print('loop is closed')

    # loop = asyncio.get_event_loop()
    # try:
    #     # запуск event loop пока не будет вызван loop.stop()
    #     loop.create_task(main())
    #     loop.run_forever()
    #     print('coroutines have finished')
    # except KeyboardInterrupt:
    #     print('manually closed application')
    # finally:
    #     loop.close()
    #     print('loop is closed')
    #     print(f'loop is closed = {loop.is_closed()}')
