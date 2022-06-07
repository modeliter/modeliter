import asyncio
from cutiepy import factories
from cutiepy.core import Supervisor


class InProcessSupervisor(Supervisor):
    async def _start(self):
        num_workers = self.supervisor_config.num_workers
        worker_config = self.supervisor_config.worker_config
        broker = self.broker

        worker_coroutines = map(
            lambda _: factories.build_worker(
                worker_config=worker_config,
                broker=broker,
            ).run(),
            range(num_workers),
        )

        await asyncio.gather(*worker_coroutines)
