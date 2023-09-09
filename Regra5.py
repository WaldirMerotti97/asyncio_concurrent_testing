from timebudget import timebudget

import adapter_four_seconds
import adapter_six_seconds
from Priority import Priority


class Regra5:

    def priority(self):
        return Priority.POSTPONED

    async def process(self, s, event):
        with timebudget('Regra 5'):
            await adapter_six_seconds.get_resultado(s, event)
            return "Regra 5"
