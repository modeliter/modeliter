from cutiepy.core import Broker


class InProcessBroker(Broker):
    async def pop_task(self):
        pass
