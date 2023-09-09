from timebudget import timebudget

import adapter_two_seconds
from Priority import Priority


class Regra2:

    def priority(self):
        return Priority.STANDARD

    async def process(self, s, event):
        with timebudget('Regra 2'):
            await adapter_two_seconds.get_resultado(s, event)
            return "Regra 2"
