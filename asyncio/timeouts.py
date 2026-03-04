import asyncio
import time


async def fetch_data(id: int, should_fail: bool = False) -> str:
    print(f'task {id} starting...')
    await asyncio.sleep(2)
    if should_fail:
        raise ValueError('Server error!')
    else:
        return f"Data {id} received!"

async def long_running_task():
    print('Running a very long task...')
    await asyncio.sleep(10)

async def main():
    start_time = time.perf_counter()

    try:
        await asyncio.wait_for(long_running_task(), timeout=3)
    except TimeoutError:
        print('Process is taking too long to run!')

    results = await asyncio.gather(
        fetch_data(id=1),
        fetch_data(id=2, should_fail=True),
        fetch_data(id=3),
        return_exceptions=True
    )

    end_time = time.perf_counter()

    print(f'results: {results}')
    print(f'total time taken: {end_time - start_time:.2f} seconds')

if __name__ == '__main__':
    asyncio.run(main())
