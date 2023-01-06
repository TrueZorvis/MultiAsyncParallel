import aiofiles
import asyncio


def count_words(text):
    return len(text.split(' '))


def read_large_file():
    with open('..\\data\\big_file.txt', 'r') as f:
        return f.read()


def main():
    text = read_large_file()
    print(count_words(text))


async def async_read_large_file():
    async with aiofiles.open('..\\data\\big_file.txt', 'r') as f:
        return await f.read()


async def async_main():
    text = await async_read_large_file()
    print(count_words(text))


if __name__ == '__main__':
    main()
    asyncio.run(async_main())
