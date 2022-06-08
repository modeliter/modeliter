import click
from cutiepy import __version__
from .run import run

@click.group()
@click.help_option("-h", "--help")
@click.version_option(__version__, "-v", "--version")
def cli_cutiepy():
    pass


cli_cutiepy.add_command(run)
