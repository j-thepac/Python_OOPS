import asyncio

async def main():
    print("Async task starting")
    await asyncio.sleep(1)
    print("Async task finished")
    return 1

# Run the async function
res = asyncio.run(main())# method 1
print(res)
# res=syncio.create_task(main())
# await res
# Advantages: Efficient for I/O-bound tasks, non-blocking execution.
