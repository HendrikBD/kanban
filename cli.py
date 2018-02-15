import click
from main import Kanban


@click.command()
@click.option('--advance', '-v', nargs=2, type=int)
@click.option('--remove', '-r', nargs=2, type=int)
@click.option('--add', '-a', nargs=1, type=str)
def cli(advance, remove, add):
    kan = Kanban()
    if(advance):
        kan.advItem(advance[0], advance[1])
    elif(remove):
        kan.removeItem(remove[0], remove[1])
    elif(add):
        kan.addItem(1, add)

    click.echo(kan.printOut())
