import asyncio
import click
from cutiepy import factories
from cutiepy.core import (
    BrokerConfig,
    SupervisorConfig,
    WorkerConfig,
)


@click.command(help="Start workers to execute tasks.")
def run():
    broker_config = BrokerConfig(
        type="sqlite",
        sqlite_uri="sqlite:///cutiepy.db",
    )
    broker = factories.build_broker(broker_config=broker_config)

    worker_config = WorkerConfig(type="inprocess")

    supervisor_config = SupervisorConfig(
        type="inprocess",
        worker_config=worker_config,
    )
    supervisor = factories.build_supervisor(
        supervisor_config=supervisor_config,
        broker=broker,
    )

    app = factories.build_app(
        broker=broker,
        supervisor=supervisor,
    )

    asyncio.run(app.start())
