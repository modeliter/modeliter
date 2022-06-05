import click
import uvicorn

from modeliter.__about__ import __version__
from modeliter.http import create_app


@click.group()
@click.help_option("-h", "--help")
@click.version_option(__version__, "-v", "--version", prog_name="modeliter")
def cli():
    pass


@cli.command(help="Run the HTTP server.")
def serve():
    uvicorn.run(
        create_app(),
        host="127.0.0.1",
        port=8000,
        log_level="info",
    )
