import os 
import click 

from .config import load_configs, get_default_configuration
from .deck import Deck 
from .utils import write_yaml

DECKS_DIR = "decks"


@click.group()
def mkslides():
    pass

# TODO: argument/option to specify output marp file
@mkslides.command('build')
def build():
    config = load_configs()

    # check for existing slide deck if configs.overwrite is False
    if config.overwrite is False and os.path.exists(config.deck.name):
        raise ValueError(f"Slide deck with name '{config.deck.name}' already exists and configs.overwrite set to 'False'.")
    
    deck = Deck(config)
    deck.build()
    
    click.echo(f"created '{config.deck.name}' from slides {', '.join(config.slides.filenames)}")


@mkslides.command('new')
@click.option('-f', '--filename')
def new(filename: str):
    new_config = get_default_configuration()
    write_yaml(filename, new_config)


if __name__ == '__main__':
    mkslides()