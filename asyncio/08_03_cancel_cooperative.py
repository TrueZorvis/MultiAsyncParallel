import asyncio
import threading


async def fetch_doc(doc):
    await asyncio.sleep(3)  # emulating doc downloading
    print(f'downloaded_{doc}')
    return doc


async def get_docs(docs, token):
    pages = []
    for cur_doc in docs:
        if token.is_set():
            break
        doc = await fetch_doc(cur_doc)
        for page in doc:
            pages.append(page)
    return pages


def get_response(token):
    reply = input('want to cancel or not? [y/n]')
    if reply == 'y':
        token.set()


async def main():
    token = threading.Event()
    tasks = asyncio.create_task(get_docs(['doc1', 'doc2', 'doc3'], token))

    t = threading.Thread(target=get_response, args=(token,))
    t.start()

    results = await tasks
    for result in results:
        print(f'{result}', end='')


if __name__ == '__main__':
    asyncio.run(main())
