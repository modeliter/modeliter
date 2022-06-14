import click
from pathlib import Path
from cutiepy.processes.supervisorprocess import SupervisorProcess
from cutiepy.brokers import SQLiteBrokerConfig, build_broker
from cutiepy.workers import WorkerConfig


@click.command(help="Starts workers for running tasks.")
def worker():
    broker_config = SQLiteBrokerConfig(
        path="./broker.sqlite",
    )
    worker_config = WorkerConfig()

    supervisor = SupervisorProcess(
        broker_config=broker_config,
        worker_config=worker_config,
    )
    supervisor.main()
