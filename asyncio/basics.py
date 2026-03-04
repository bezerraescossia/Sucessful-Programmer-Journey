import asyncio


async def fetch_data() -> str:
    await asyncio.sleep(5)
    return "Data received!"

result = asyncio.run(fetch_data())
print(result)
