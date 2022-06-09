import os
import signal
from multiprocessing import Process, Pipe
import time
from pydantic.dataclasses import dataclass
from typing import Any, Optional, Callable



@dataclass
class WorkerConfig:
    pass

@dataclass
class Runner:
    worker_config: WorkerConfig
    config_conn: Any
    shutdown_conn: Any
    should_shutdown: bool = False

    def main(self):
        # Setup this runner process.
        self._install_signal_handlers(handler=self._begin_shutdown)

        # Main loop.
        while not self.should_shutdown:
            if self.config_conn.poll():
                self.worker_config = self.config_conn.recv()
            
            self.tick()

            if self.shutdown_conn.poll():
                self.should_shutdown = self.shutdown_conn.recv()

        # Shutdown.
        self.config_conn.close()
        self.shutdown_conn.close()

    def tick(self):
        time.sleep(1)

    def _install_signal_handlers(self, handler: Callable):
        signals = [signal.SIGINT, signal.SIGTERM, signal.SIGHUP]
        for s in signals:
            signal.signal(s, handler)

    def _begin_shutdown(self, _signum, _frame):
        print("Runner is shutting down...")
        self.should_shutdown = True

    def _force_shutdown(self, _signum, _frame):
        raise RuntimeError("Worker forced shutdown.")

def target_runner_process(
    *,
    worker_config: WorkerConfig,
    config_conn: Any,
    shutdown_conn: Any,
    ):
    Runner(
        worker_config=worker_config,
        config_conn=config_conn,
        shutdown_conn=shutdown_conn,
    ).main()

@dataclass
class Worker:
    worker_config: WorkerConfig
    should_shutdown: bool = False

    def main(self):
        # Setup this worker process.
        self._install_signal_handlers(handler=self._begin_shutdown)
        self._sync_with_broker()

        # Setup and spawn a runner process.
        runner_config_conn, child_config_conn = Pipe()
        runner_shutdown_conn, child_shutdown_conn = Pipe()
        runner = Process(
            target=target_runner_process,
            kwargs={
                "worker_config": self.worker_config,
                "config_conn": child_config_conn,
                "shutdown_conn": child_shutdown_conn,
            },
        )
        runner.start()

        # Main loop.
        while not self.should_shutdown:
            worker_config = self._sync_with_broker()
            runner_config_conn.send(worker_config)
            time.sleep(1)

        # Gracefully shutdown.
        self._install_signal_handlers(handler=self._force_shutdown)
        runner.join()
        runner_config_conn.close()
        runner_shutdown_conn.close()

    def _sync_with_broker(self):
        pass

    def _install_signal_handlers(self, handler: Callable):
        signals = [signal.SIGINT, signal.SIGTERM, signal.SIGHUP]
        for s in signals:
            signal.signal(s, handler)

    def _begin_shutdown(self, _signum, _frame):
        print("Worker is shutting down...")
        self.should_shutdown = True

    def _force_shutdown(self, _signum, _frame):
        raise RuntimeError("Worker forced shutdown.")


def target_worker_process(*, worker_config: WorkerConfig):
    Worker(worker_config).main()

@dataclass
class Supervisor:
    worker_config: WorkerConfig
    num_workers: int = 1
    should_shutdown: bool = False

    def main(self):
        # Setup this supervisor process.
        self._install_signal_handlers(handler=self._begin_shutdown)

        # Spawn and supervise the worker processes.
        workers: list[Process] = [None] * self.num_workers
        while not self.should_shutdown:
            for i in range(self.num_workers):
                if workers[i] is None:
                    print(f"Starting worker [{i}]")
                    workers[i] = self._spawn_worker()

                if not workers[i].is_alive():
                    print(f"Restarting dead worker [{i}]")
                    workers[i] = self._spawn_worker()

            time.sleep(1)

        # Gracefully shutdown.
        self._install_signal_handlers(handler=self._force_shutdown)
        for worker in workers:
            worker.join()

    def _spawn_worker(self) -> Process:
        worker = Process(
            target=target_worker_process,
            kwargs={"worker_config": self.worker_config},
        )
        worker.start()
        return worker

    def _install_signal_handlers(self, handler: Callable):
        signals = [signal.SIGINT, signal.SIGTERM, signal.SIGHUP]
        for s in signals:
            signal.signal(s, handler)

    def _begin_shutdown(self, _signum, _frame):
        print("Supervisor is shutting down...")
        self.should_shutdown = True

    def _force_shutdown(self, _signum, _frame):
        raise RuntimeError("Supervisor forced shutdown.")

if __name__ == "__main__":
    worker_config = WorkerConfig()
    Worker(worker_config).main()
