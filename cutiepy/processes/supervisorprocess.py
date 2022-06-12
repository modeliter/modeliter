from typing import Any
from dataclasses import dataclass
from multiprocessing import Pipe, Process
import signal
import time
from cutiepy.brokers import BrokerConfig, build_broker
from cutiepy.workers import WorkerConfig


@dataclass
class RunnerProcess:
    broker_config: BrokerConfig
    worker_config: WorkerConfig
    config_conn: Any
    shutdown_conn: Any
    should_shutdown: bool = False

    def __post_init__(self):
        self.process = Process(target=self._main)

    def start(self):
        return self.process.start()

    def join(self):
        return self.process.join()

    def is_alive(self):
        return self.process.is_alive()

    def _main(self):
        # Setup this runner process.
        self._install_signal_handlers()

        # Main loop.
        while not self.should_shutdown:
            if self.config_conn.poll():
                self.worker_config = self.config_conn.recv()
            
            self.tick()

            if self.shutdown_conn.poll():
                self.should_shutdown = self.shutdown_conn.recv()

        # Gracefully shutdown.
        self.config_conn.close()
        self.shutdown_conn.close()

    def tick(self):
        print("Runner tick")
        broker = build_broker(broker_config=self.broker_config)
        time.sleep(1)

    def _install_signal_handlers(self):
        signals = [signal.SIGINT, signal.SIGTERM, signal.SIGHUP]
        for s in signals:
            signal.signal(s, self._begin_shutdown)

    def _begin_shutdown(self, _signum, _frame):
        self.should_shutdown = True


@dataclass
class WorkerProcess:
    broker_config: BrokerConfig
    worker_config: WorkerConfig
    should_shutdown: bool = False

    def __post_init__(self):
        self.process = Process(target=self._main)

    def start(self):
        return self.process.start()

    def join(self):
        return self.process.join()

    def is_alive(self):
        return self.process.is_alive()

    def _main(self):
        # Setup this worker process.
        self._install_signal_handlers()
        self._sync_with_broker()

        # Setup and spawn a runner process.
        runner_config_conn, child_config_conn = Pipe()
        runner_shutdown_conn, child_shutdown_conn = Pipe()
        runner_process = RunnerProcess(
            broker_config=self.broker_config,
            worker_config=self.worker_config,
            config_conn=child_config_conn,
            shutdown_conn=child_shutdown_conn,
        )
        runner_process.start()

        # Main loop.
        while not self.should_shutdown:
            worker_config = self._sync_with_broker()
            runner_config_conn.send(worker_config)

        # Gracefully shutdown.
        runner_process.join()
        runner_config_conn.close()
        runner_shutdown_conn.close()

    def _sync_with_broker(self):
        time.sleep(1)

    def _install_signal_handlers(self):
        signals = [signal.SIGINT, signal.SIGTERM, signal.SIGHUP]
        for s in signals:
            signal.signal(s, self._begin_shutdown)

    def _begin_shutdown(self, _signum, _frame):
        self.should_shutdown = True


@dataclass
class SupervisorProcess:
    broker_config: BrokerConfig
    worker_config: WorkerConfig
    num_workers: int = 1
    should_shutdown: bool = False

    def main(self):
        # Setup this supervisor process.
        self._install_signal_handlers()

        # Spawn and supervise the worker processes.
        worker_processes: list[Process] = [None] * self.num_workers
        while not self.should_shutdown:
            for i in range(self.num_workers):
                if worker_processes[i] is None:
                    print(f"Starting worker [{i}]")
                    worker_processes[i] = self._spawn_worker()

                if not worker_processes[i].is_alive():
                    print(f"Restarting dead worker [{i}]")
                    worker_processes[i] = self._spawn_worker()

            time.sleep(1)

        # Gracefully shutdown.
        for worker_process in worker_processes:
            worker_process.join()

    def _spawn_worker(self) -> WorkerProcess:
        worker_process = WorkerProcess(
            broker_config=self.broker_config,
            worker_config=self.worker_config,
        )
        worker_process.start()
        return worker_process

    def _install_signal_handlers(self):
        signals = [signal.SIGINT, signal.SIGTERM, signal.SIGHUP]
        for s in signals:
            signal.signal(s, self._begin_shutdown)

    def _begin_shutdown(self, _signum, _frame):
        print("Supervisor: shutting down...")
        self.should_shutdown = True
