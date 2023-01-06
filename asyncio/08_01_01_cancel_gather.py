import asyncio
import threading
import time
import aiohttp
from asyncio.exceptions import CancelledError


class Photo:
    def __init__(self, album_id, photo_id, title, url, thumbnail_url):
        self.album_id = album_id
        self.photo_id = photo_id
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url

    @classmethod
    def from_json(cls, obj):
        return Photo(obj['albumId'], obj['id'], obj['title'], obj['url'], obj['thumbnailUrl'])


def print_photo_titles(photos):
    for photo in photos:
        print(f'{photo.title}', end='\n')


async def photos_by_album(task_name, album, session):
    print(f'{task_name=}')
    url = f'https://jsonplaceholder.typicode.com/photos?albumId={album}'

    if not isinstance(album, int):
        await asyncio.sleep(2)
        raise TypeError('Invalid album number type')

    response = await session.get(url)
    photos_json = await response.json()

    sleeping_period = 3 if task_name == 't3' else 1
    print(f'{task_name=} sleeping')
    await asyncio.sleep(sleeping_period)
    print(f'{task_name=} finished sleeping')

    print(f'Finished task={task_name}')
    return [Photo.from_json(photo) for photo in photos_json]


def get_coros(session):
    return [
        photos_by_album('t1', 1, session),
        photos_by_album('t2', 2, session),
        photos_by_album('t3', 3, session),
        photos_by_album('t4', 4, session),
    ]


def cancel_future(loop, future, after):
    def inner_cancel():
        print('sleeping before future cancel')
        time.sleep(after)
        print('cancel future')
        loop.call_soon_threadsafe(future.cancel)

    t = threading.Thread(target=inner_cancel)
    t.start()


def cancel_task(tasks, after):
    def inner_cancel():
        print('sleeping before task cancel')
        time.sleep(after)
        print('cancel task')
        for i, t in enumerate(tasks):
            print(f'cancel {i}, {t}')
            res = t.cancel()
            print(f'cancelling result: {res}')

    t = threading.Thread(target=inner_cancel)
    t.start()


async def main_gather_cancel_on_future():
    async with aiohttp.ClientSession() as session:
        future = asyncio.gather(*(get_coros(session)))

        cancel_future(asyncio.get_running_loop(), future, 2)

        try:
            print('awaiting future')
            result = await future
        except CancelledError as ex:
            print(f'Excepted at await {repr(ex)}')


async def main_gather_cancel_on_tasks():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(coro) for coro in get_coros(session)]
        future = asyncio.gather(*tasks)

        cancel_task(tasks, 2)

        try:
            print('awaiting future')
            result = await future
        except CancelledError as ex:
            print(f'Excepted at await {repr(ex)}')


async def main_gather_return_exceptions():
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(coro) for coro in get_coros(session)]
        future = asyncio.gather(*tasks, return_exceptions=True)

        cancel_task(tasks, 2)

        try:
            print('awaiting future')
            results = await future
            for result in results:
                if isinstance(result, CancelledError):
                    print(repr(result))
                else:
                    print_photo_titles(result)
            print('after for')
        except CancelledError as ex:
            print(f'Excepted at await {repr(ex)}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    try:
        # loop.create_task(main_gather_cancel_on_future())
        # loop.create_task(main_gather_cancel_on_tasks())
        loop.create_task(main_gather_return_exceptions())
        loop.run_forever()
    finally:
        print('closing loop')
        loop.close()
