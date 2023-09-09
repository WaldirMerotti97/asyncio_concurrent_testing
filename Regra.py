import uuid

from timebudget import timebudget

import adapter_four_seconds
from Priority import Priority


class Regra:

    def priority(self) -> Priority:
        return Priority.STANDARD

    async def process(self, s, event):
        with timebudget('Regra 1'):
            await adapter_four_seconds.get_resultado(s, event)
            return "Regra 1"
