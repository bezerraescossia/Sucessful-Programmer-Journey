import asyncio
from typing import List

async def retrieve_source(source_name: str, delay: float) -> str | None:
    print(f"Retrieving from {source_name}...")
    try:
        # We apply the timeout INSIDE the task itself
        return await asyncio.wait_for(
            asyncio.sleep(delay, result=f"[{source_name} context]"), 
            timeout=2.5
        )
    except asyncio.TimeoutError:
        print(f"Warning: {source_name} timed out!")
        return None # Return None so we can filter it out later

async def generate_answer(context_list: List[str]) -> str:
    print("Generating final answer with available context...")
    await asyncio.sleep(1)
    return " ".join(context_list)

async def main():
    # Run all retrievals concurrently
    results = await asyncio.gather(
        retrieve_source('A', 1.0),
        retrieve_source('B', 5.0), # This will timeout
        retrieve_source('C', 0.5),
    )

    # Filter out the 'None' values from timed-out sources
    successful_context = [res for res in results if res is not None]
    
    # Generate answer with what we have
    answer = await generate_answer(successful_context)
    print(f"\nFinal AI Answer: {answer}")

if __name__ == '__main__':
    asyncio.run(main())