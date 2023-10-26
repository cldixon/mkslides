import os 
import click 

from .config import load_config, create_new_configuration_file
from .deck import Deck 


@click.group()
def mkslides():
    pass

# TODO: argument/option to specify output marp file
@mkslides.command('build')
@click.option('-f', '--filename')
def build(filename: str):
    config = load_config(filename)

    # check for existing slide deck if configs.overwrite is False
    if config.overwrite is False and os.path.exists(config.name):
        raise ValueError(f"Slide deck with name '{config.name}' already exists and configs.overwrite set to 'False'.")
    
    deck = Deck(config)
    deck.build()
    
    click.echo(f"created '{config.name}' from {len(config.slides):,} slides.")


@mkslides.command('new')
@click.option('-f', '--filename')
def new(filename: str):
    create_new_configuration_file(filename)


if __name__ == '__main__':
    mkslides()