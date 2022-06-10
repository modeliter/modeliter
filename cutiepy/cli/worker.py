import click
from cutiepy import factories
from cutiepy.supervisor import Supervisor
from cutiepy.core import BrokerConfig, WorkerConfig


@click.command(help="Starts workers for running tasks.")
def worker():
    broker_config = BrokerConfig(
        type="sqlite",
        sqlite_uri="sqlite:///cutiepy.db",
    )
    broker = factories.build_broker(broker_config=broker_config)
    worker_config = WorkerConfig()

    supervisor = Supervisor(
        broker=broker,
        worker_config=worker_config,
    )
    supervisor.main()
