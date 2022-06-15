def main():
    from cutiepy.cli import build_cutiepy_cli as build_cli
    from sys import exit

    cutiepy_cli = build_cli()
    exit(cutiepy_cli())
