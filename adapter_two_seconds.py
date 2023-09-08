import asyncio


async def get_resultado(s):
    async with s.get('https://www.google.com.br') as r:
        await asyncio.sleep(2)  # non-blocking
        # sleep(2) # blocking
        if r.status != 200:
            r.raise_for_status()
        return await r.text()
