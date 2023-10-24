import os 
import subprocess
from typing import List, Literal, Union
from dataclasses import dataclass, asdict

from .config import MkSlidesConfig, Directives
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

def compile_directives(theme: str = 'default', paginate: bool = False, header: str = None, footer: str = None) -> str:
    # add theme
    directives = [
        f"theme: {theme}"
    ]
    # add pagination
    if paginate is True:
        directives.append("paginate: true")
    # add header
    if header:
        directives.append(f"header: {header}")
    if footer:
        directives.append(f"footer: {footer}")

    directives = "\n".join(directives)
    return f"{SLIDE_SEP}\n{directives}\n{SLIDE_SEP}"
    

def compile_slides(slides: List[str]) -> str:
    # combine slides into single text
    return f"\n{SLIDE_SEP}\n\n".join(slides) 

@dataclass
class Directives:
    theme: Literal["default", "gaia", "uncover"]
    paginate: bool
    header: Union[str, None]
    footer: Union[str, None]

    def to_dict(self) -> dict:
        return asdict(self)


class Deck:
    def __init__(self, config: MkSlidesConfig):
        self.name: str = config.name
        self.description: str = config.description
        self.author: str = config.author 
        self.output_dir: str = config.output_dir
        self.slides: List[str] = open_files(config.slides)
        self.directives: Directives = Directives(
            theme=config.theme,
            paginate=config.paginate,
            header=config.header,
            footer=config.footer
        )   

    def assemble_slides(self) -> None:
        """Build deck from slides, configurations, etc."""
        _directives = compile_directives(**self.directives.to_dict())
        _content = compile_slides(self.slides)
        self.content = f"{_directives}\n\n{_content}"
        
    
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