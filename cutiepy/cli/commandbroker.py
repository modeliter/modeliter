import click

@click.command(name="broker", help="Start the broker server.")
def command_broker():
    print("Hello broker!")
