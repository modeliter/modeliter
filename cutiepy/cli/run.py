import asyncio
import click
from cutiepy import factories
from cutiepy.core import (
    BrokerConfig,
    DashboardServerConfig,
    SupervisorConfig,
    WorkerConfig,
)

@click.command(help="Run workers and/or the dashboard web server.")
def run():
    broker_config = BrokerConfig(
        type="inprocess",
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

    dashboard_server_config = DashboardServerConfig(
        type="inprocess",
    )
    dashboard_server = factories.build_dashboard_server(
        dashboard_server_config=dashboard_server_config,
        broker=broker,
        supervisor=supervisor,
    )

    app = factories.build_app(
        broker=broker,
        supervisor=supervisor,
        dashboard_server=dashboard_server,
    )

    asyncio.run(app.start())
