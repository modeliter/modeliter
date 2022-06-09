import click
from cutiepy import factories

from cutiepy.dashboardserver import build_app
import uvicorn


@click.command(help="Start dashboard server to monitor tasks and workers.")
def dashboard():
    broker_config = BrokerConfig(
        type="sqlite",
        sqlite_uri="sqlite:///cutiepy.db",
    )
    broker = factories.build_broker(broker_config=broker_config)

    app = build_app(broker=broker, debug=True)
    uvicorn.run(
        app=app,
        host="127.0.0.1",
        port=8000,
        log_level="info",
    )
