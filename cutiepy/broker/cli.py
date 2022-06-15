import click
from cutiepy.broker.http_api import build_broker_http_api_app as build_app
import uvicorn

def build_broker_cli():
    @click.command(name="broker")
    def broker_cli():
        uvicorn.run(app=build_app())

    return broker_cli
