import click
from cutiepy import __version__
from .worker import worker

@click.group()
@click.help_option("-h", "--help")
@click.version_option(__version__, "-v", "--version")
def cli_cutiepy():
    pass


cli_cutiepy.add_command(worker)
