# this is an asyn web scraper, that uses aiohttp , a asyn compliant library like requests
import asyncio
import math
import aiofiles
import aiohttp
import time


async def fetch(url):
    if url == "https://python.org":
        await asyncio.sleep()

    print(f"fetching for {url} ....")
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        html = await response.text()
        return html


# defining another coroutine that writes some text to a file
async def write_to_file(file, text):
    print(f"writing text output for {file} ...")
    async with aiofiles.open(file, "w") as f:
        await f.write(text)


async def main(urls):
    text_responses = await asyncio.gather(*[fetch(url) for url in urls])
    await asyncio.gather(
        *[
            write_to_file(f'{url.split("//")[-1]}.txt', text_response)
            for url, text_response in zip(urls, text_responses)
        ]
    )


asyncio.run(
    main(["https://python.org", "https://stackoverflow.com", "https://google.com"])
)
