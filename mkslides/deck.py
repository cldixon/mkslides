import os 
from .config import Config
from .utils import open_files, save_to_file

SLIDE_SEP = "---"
DEFAULT_DECK_DIR = "decks"


class Deck:
    def __init__(self, config: Config):
        self.name = config.deck.name
        self.description = config.deck.description
        self.author = config.deck.author
        self.theme = config.theme
        self.output_dir = DEFAULT_DECK_DIR
        self.slides = open_files(config.slides.full_paths)

    def build(self) -> None:
        """Build deck from slides, configurations, etc."""
        self.content = f"\n{SLIDE_SEP}\n".join(self.slides) 
    
    def save(self) -> None:
        save_to_file(os.path.join(self.output_dir, self.name), self.content)

    def build_and_save(self) -> None:
        self.build()
        self.save()