import click
from cutiepy.broker.cli import build_broker_cli
from cutiepy.__version__ import __version__

def build_cutiepy_cli() -> click.Command:
    @click.group(name="cutiepy")
    @click.help_option("-h", "--help")
    @click.version_option(__version__, "-v", "--version")
    def cli():
        pass

    cli.add_command(build_broker_cli())

    return cli
