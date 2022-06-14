import click

from cutiepy.dashboardserver import build_app
import uvicorn


@click.command(help="Start dashboard server to monitor tasks and workers.")
def dashboard():
    app = build_app(broker=broker, debug=True)
    uvicorn.run(
        app=app,
        host="127.0.0.1",
        port=8000,
        log_level="info",
    )
