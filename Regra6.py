from timebudget import timebudget

import adapter_four_seconds
from Priority import Priority


class Regra:

    def priority(self):
        return Priority.POSTPONED

    async def process(self, s):
        with timebudget('Regra 1'):
            await adapter_four_seconds.get_resultado(s)
            return "Regra 1"
