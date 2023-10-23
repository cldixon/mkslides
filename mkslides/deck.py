import os 
import subprocess

from .config import MkSlidesConfig
from .utils import open_files, save_to_file

SLIDE_SEP = "---"
DEFAULT_DECK_DIR = "decks"


def run_marp_cli(filepath: str) -> None:
    """Run MARP as Python subprocess, with provided filename."""
    _ = subprocess.run(
        ["marp", filepath],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    )
    return 


class Deck:
    def __init__(self, config: MkSlidesConfig):
        self.name = config.deck.name
        self.description = config.deck.description
        self.author = config.deck.author
        self.theme = config.theme
        self.output_dir = DEFAULT_DECK_DIR
        self.slides = open_files(config.slides.full_paths)

    def assemble_slides(self) -> None:
        """Build deck from slides, configurations, etc."""
        self.content = f"\n{SLIDE_SEP}\n".join(self.slides) 
    
    def save_markdown_slides(self) -> None:
        save_to_file(
            os.path.join(self.output_dir, self.name), 
            self.content
        )

    def convert_with_marp(self):
        run_marp_cli(os.path.join(self.output_dir, self.name))

    def build(self) -> None:
        self.assemble_slides()
        self.save_markdown_slides()
        self.convert_with_marp()