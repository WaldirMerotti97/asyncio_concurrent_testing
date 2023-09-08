# "threading is for working in parallel, and async is for waiting in parallel".


import asyncio
from time import perf_counter, sleep
from typing import List

import aiohttp

from Regra import Regra
from Regra2 import Regra2
from Regra3 import Regra3


async def executa_regra(s, regra):
    return await regra.process(s)


async def executa_regras(s, regras):
    tasks = []
    for regra in regras:
        task = asyncio.create_task(executa_regra(s, regra))
        tasks.append(task)
    res = await asyncio.gather(*tasks)
    return res


async def main():
    regras: List[Regra] = [Regra(), Regra2(), Regra3()]
    async with aiohttp.ClientSession() as session:
        resultados = await executa_regras(session, regras)
        print(f'Regras Processadas: {resultados}')


if __name__ == '__main__':
    start = perf_counter()
    asyncio.run(main())
    stop = perf_counter()
    print("time taken:", stop - start)
