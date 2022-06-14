import click
from cutiepy import __version__
from cutiepy.cli.commandbroker import command_broker

@click.group
@click.help_option("-h", "--help")
@click.version_option(__version__, "-v", "--version")
def cutiepy_cli():
    pass

cutiepy_cli.add_command(command_broker)
