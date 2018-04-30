import click

@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    """This script prints hello NAME COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)
