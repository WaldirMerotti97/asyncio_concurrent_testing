import asyncio

from async_lru import alru_cache


@alru_cache(ttl=30)
async def get_resultado(s, event):
    async with s.get('https://www.google.com.br') as r:
        await asyncio.sleep(2)  # non-blocking
        # sleep(2) # blocking
        if r.status != 200:
            r.raise_for_status()
        return await r.text()
