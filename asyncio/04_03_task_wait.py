import asyncio
from collections import namedtuple

import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

services = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)


async def get_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_ip(service):
    print(f'Fetching IP from {service.name}')

    json_responce = await get_json(service.url)
    ip = json_responce[service.ip_attr]

    return f'{service.name} finished with result: {ip}'


async def main():
    coros = [asyncio.create_task(fetch_ip(service)) for service in services]
    done, ponding = await asyncio.wait(coros)

    # первый результат, остальные результаты не увидим
    # done, ponding = await asyncio.wait(coros, return_when=asyncio.FIRST_COMPLETED)

    for x in done:
        print(x.result())


if __name__ == '__main__':
    asyncio.run(main())
