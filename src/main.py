import asyncio
from utils import common


async def callphone(ms: int):
    common.say_hello("Hello world!")
    await asyncio.sleep(ms)
    common.say_hello("Hello again!")


async def application():
    await callphone(2)


task = application()
asyncio.run(task)
