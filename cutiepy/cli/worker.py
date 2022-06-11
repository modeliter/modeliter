import click
from cutiepy.processes.supervisorprocess import SupervisorProcess
from cutiepy.brokers import SQLiteBrokerConfig, build_broker
from cutiepy.workers import WorkerConfig


@click.command(help="Starts workers for running tasks.")
def worker():
    broker_config = SQLiteBrokerConfig(
        path="sqlite:///cutiepy.db",
    )
    broker = build_broker(broker_config=broker_config)
    worker_config = WorkerConfig()

    supervisor = SupervisorProcess(
        broker=broker,
        worker_config=worker_config,
    )
    supervisor.main()
