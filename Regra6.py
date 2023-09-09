from timebudget import timebudget

import adapter_four_seconds
from Priority import Priority


class Regra6:

    def priority(self):
        return Priority.POSTPONED

    async def process(self, s, event):
        with timebudget('Regra 6'):
            await adapter_four_seconds.get_resultado(s, event)
            return "Regra 6"
