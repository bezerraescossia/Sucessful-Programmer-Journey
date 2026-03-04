import asyncio
import time


async def fetch_data(id: int) -> str:
    print(f'task {id} starting...')
    await asyncio.sleep(2)
    return f"Data {id} received!"

async def main():
    start_time = time.perf_counter()
    results = await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    end_time = time.perf_counter()

    print(f'results: {results}')
    print(f'total time taken: {end_time - start_time:.2f} seconds')

if __name__ == '__main__':
    asyncio.run(main())
