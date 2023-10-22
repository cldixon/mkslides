import os 
import click 

from .config import load_configs
from .deck import Deck 

DECKS_DIR = "decks"

@click.group()
def mkslides():
    pass

@mkslides.command('build')
def build():
    config = load_configs()


    # check for existing slide deck if configs.overwrite is False
    if config.overwrite is False and os.path.exists(config.deck.name):
        raise ValueError(f"Slide deck with name '{config.deck.name}' already exists and configs.overwrite set to 'False'.")
    
    deck = Deck(config)
    deck.build_and_save()
    
    click.echo(f"created '{config.deck.name}' from slides {', '.join(config.slides.filenames)}")

if __name__ == '__main__':
    mkslides()