import threading
import asyncio
from concurrent.futures import ThreadPoolExecutor
from queue import Queue


async def async_fn():
    await asyncio.sleep(1)
    print(f"async_fn waited for 1 sec : {threading.get_native_id()}")

def main(*args):
    print(args)
    asyncio.run(async_fn())


q=Queue
q.put(1)
q.put(2)
t=threading.Thread(target=main,args=(1,2))
t.start()
t.join()

with ThreadPoolExecutor(1) as e:
    res=e.map(main,[(1,2)])