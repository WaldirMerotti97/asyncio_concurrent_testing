from timebudget import timebudget

import adapter_four_seconds
import adapter_six_seconds
from Priority import Priority


class Regra:

    def priority(self):
        return Priority.POSTPONED

    async def process(self, s):
        with timebudget('Regra 1'):
            await adapter_six_seconds.get_resultado(s)
            return "Regra 1"