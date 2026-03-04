import asyncio

from asyncio import Queue
from typing import Any
from time import perf_counter


async def producer(queue: Queue[Any]):
    for item in range(1, 6):
            await asyncio.sleep(0.1) # Simulate slight delay in production
            await queue.put(item)
            print(f"Produced item {item}")

async def consumer(name: str, queue: Queue[Any]):
    while True:
        # Get a "work item" out of the queue.
        item = await queue.get()
        print(f"Consumer {name} processing item {item}...")
        
        await asyncio.sleep(1) # Simulate 1 second of work
        
        # Notify the queue that the item has been processed.
        queue.task_done()
        print(f"Consumer {name} finished item {item}")
    
async def main():
    queue: Queue[Any] = Queue()
    start_time = perf_counter()

    # 1. Start the consumers in the background using create_task
    # These will now run "concurrently" with the rest of main()
    c1 = asyncio.create_task(consumer("A", queue))
    c2 = asyncio.create_task(consumer("B", queue))

    # 2. Run the producer and wait for it to finish putting items in
    await producer(queue)

    # 3. Wait until the queue is fully processed (all task_done calls made)
    await queue.join()

    # 4. Since consumers are in an infinite 'while True' loop, 
    # we stop them now that the work is done.
    c1.cancel()
    c2.cancel()

    end_time = perf_counter()
    print(f"Total time for 5 items with 2 consumers: {end_time - start_time:.2f} seconds")

if __name__ == '__main__':
    asyncio.run(main())
