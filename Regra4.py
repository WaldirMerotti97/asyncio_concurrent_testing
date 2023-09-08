from timebudget import timebudget

import adapter_two_seconds
from Priority import Priority


class Regra:

    def priority(self):
        return Priority.POSTPONED

    async def process(self, s):
        with timebudget('Regra 1'):
            await adapter_two_seconds.get_resultado(s)
            return "Regra 1"
