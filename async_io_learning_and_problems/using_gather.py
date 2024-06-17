import asyncio
import time


def normal():
    print("here ..")
    return 1


"""
async def one():
    print("inside one ...")
    # await normal() cannot do ths , we need to await on an async only
    x = await two()
    return x


async def two():
    print("inside two ...")
    x = await three()
    return x


async def three():
    print("inside three ...")
    await asyncio.sleep(5)
    return 3


async def main():
    # this is the top - level coroutine for our program
    # asyncio.gather(one())
    final_ans = await one()
    print(final_ans)


# statement to create the event loop and run the main coroutine
asyncio.run(main())
"""


async def one():
    print("inside one ...")
    # await normal() cannot do ths , we need to await on an async only
    return 1


async def two():
    print("inside two ...")
    return 2


async def three():
    print("inside three ...")
    await asyncio.sleep(2)
    return 3


async def main():
    # this is the top - level coroutine for our program
    # in gather even if the crs are not performed in order, they will be returned as a wrapped future in order
    wrapped_future_result = await asyncio.gather(three(), one(), two(), three())
    print(wrapped_future_result)


# statement to create the event loop and run the main coroutine
asyncio.run(main())
