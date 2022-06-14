from .worker import Worker, WorkerConfig


def build_worker(*, worker_config):
    return Worker(worker_config=worker_config)
