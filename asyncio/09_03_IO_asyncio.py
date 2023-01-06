import asyncio

import requests
import aiohttp
from multithreading.decorators import async_measure_time


async def download_site(url, session):
    async with session.get(url) as response:
        print(f'read {response.content.total_bytes} from {url}')


@async_measure_time
async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(download_site(url, session)) for url in sites]

        try:
            print('before await')
            await asyncio.gather(*tasks, return_exceptions=True)
        except Exception as ex:
            print(repr(ex))


if __name__ == '__main__':
    sites = [
        "https://www.engineerspock.com",
        "https://enterprisecraftsmanship.com",
    ] * 80

    asyncio.run(download_all_sites(sites))
