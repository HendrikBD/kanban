import click
from main import Kanban


@click.command()
def cli():
    kan = Kanban()
    click.echo(kan.printOut())
