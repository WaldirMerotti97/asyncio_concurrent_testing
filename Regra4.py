from timebudget import timebudget

import adapter_two_seconds
from Priority import Priority


class Regra4:

    def priority(self):
        return Priority.POSTPONED

    async def process(self, s, event):
        with timebudget('Regra 4'):
            await adapter_two_seconds.get_resultado(s, event)
            return "Regra 4"
