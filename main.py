# "threading is for working in parallel, and async is for waiting in parallel".


import asyncio
from typing import List

import aiohttp

from Priority import Priority
from Regra import Regra
from Regra2 import Regra2
from Regra3 import Regra3
from Regra4 import Regra4
from Regra5 import Regra5
from Regra6 import Regra6
from event_data import event_data


async def executa_regra(s, regra, event):
    return await regra.process(s, event)


async def executa_regras(s, regras: List[Regra], event):
    tasks = []

    regras_standard = list(filter(lambda r: r.priority() == Priority.STANDARD, regras))
    regras_postponed = list(filter(lambda r: r.priority() == Priority.POSTPONED, regras))

    for regra in regras_standard:
        task = asyncio.create_task(executa_regra(s, regra, event))
        tasks.append(task)
    rules_processed = await asyncio.gather(*tasks)

    tasks.clear()

    for regra in regras_postponed:
        task = asyncio.create_task(executa_regra(s, regra, event))
        tasks.append(task)
    rules_postponed_processed = await asyncio.gather(*tasks)

    rules_processed.extend(rules_postponed_processed)
    return rules_processed


async def main(event):
    regras: List[Regra] = [Regra(), Regra2(), Regra3(), Regra4(), Regra5(), Regra6()]
    async with aiohttp.ClientSession() as session:
        resultados = await executa_regras(session, regras, event)
        print(f'Regras Processadas: {resultados}')


if __name__ == '__main__':
    asyncio.run(main(event_data.get('identifier')))
