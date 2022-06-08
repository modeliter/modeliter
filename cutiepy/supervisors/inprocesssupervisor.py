import asyncio
from cutiepy import factories
from cutiepy.core import Supervisor


class InProcessSupervisor(Supervisor):
    async def _start(self):
        num_workers = self.supervisor_config.num_workers
        worker_config = self.supervisor_config.worker_config
        broker = self.broker

        worker_coroutines = []
        for _ in range(num_workers):
            worker = factories.build_worker(
                worker_config=worker_config,
                broker=broker,
            )
            worker_coroutines.append(worker.start())

        await asyncio.gather(*worker_coroutines)
