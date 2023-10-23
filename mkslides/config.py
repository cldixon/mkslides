import os 
from typing import List, Optional
from pydantic import BaseModel, StrictStr
from pydantic.dataclasses import dataclass 

from .utils import read_yaml

DEFAULT_SLIDES_DIR = "slides"
DEFAULT_CONFIGS_FILENAME = "mkslides.yml"



class Deck(BaseModel):
    name: StrictStr
    description: StrictStr
    author: StrictStr

@dataclass
class Slides():
    filenames: List[str]
    _dir: StrictStr = DEFAULT_SLIDES_DIR

    def __post_init__(self):
        self.full_paths = [os.path.join(self._dir, f) for f in self.filenames]

class Directives(BaseModel):
    theme: StrictStr = "default"
    paginate: bool = False
    header: Optional[str] = None
    footer: Optional[str] = None


class MkSlidesConfig(BaseModel):
    deck: Deck
    directives: Directives
    overwrite: bool
    slides: Slides


def load_configs(filename: str = DEFAULT_CONFIGS_FILENAME) -> MkSlidesConfig:
    _configs = read_yaml(filename)
    return MkSlidesConfig(
        deck=Deck(
            name=_configs.get("name"),
            description=_configs.get("description"),
            author=_configs.get("author")
        ),
        directives=Directives(
            theme=_configs.get("theme"),
            paginate=_configs.get("paginate"),
            header=_configs.get("header"),
            footer=_configs.get("footer")
        ),
        overwrite=_configs["overwrite"],
        slides=Slides(filenames=_configs["slides"])
    )


def get_default_configuration() -> dict:
    return {
        "deck": {
            "name": "my-slide-deck.md",
            "description": "First deck developed by mkslides.",
            "author": "Your name here, please!"
        },
        "theme": "default",
        "overwrite": True,
        "slides": [
            "slide_numero_uno.md"
        ]
    }