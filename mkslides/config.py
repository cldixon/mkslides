import os 
from typing import List
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


class MkSlidesConfig(BaseModel):
    deck: Deck
    theme: StrictStr
    overwrite: bool
    slides: Slides


def load_configs(filename: str = DEFAULT_CONFIGS_FILENAME) -> MkSlidesConfig:
    _configs = read_yaml(filename)
    return MkSlidesConfig(
        deck=Deck(**_configs["deck"]),
        theme=_configs["theme"],
        overwrite=_configs["overwrite"],
        slides=Slides(filenames=_configs["slides"])
    )