import asyncio
from time import sleep


async def get_resultado(s):
    async with s.get('https://www.google.com.br') as r:
        await asyncio.sleep(4)  # non-blocking
        # sleep(4) # blocking
        if r.status != 200:
            r.raise_for_status()
        return await r.text()
