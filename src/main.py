import asyncio

print("Hello Python")


async def say_hello(ms: int):
    print("Hello world!")
    await asyncio.sleep(ms)
    print("Hello again!")


async def application():
    await say_hello(2)


task = application()
asyncio.run(task)
