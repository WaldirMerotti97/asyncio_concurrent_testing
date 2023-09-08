from timebudget import timebudget

import adapter_six_seconds
from Priority import Priority


class Regra3:

    def priority(self):
        return Priority.STANDARD

    async def process(self, s):
        with timebudget('Regra 3'):
            await adapter_six_seconds.get_resultado(s)
            return "Regra 3"
