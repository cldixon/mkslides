import os
from typing import List, Literal, Optional, Union

from pydantic import BaseModel, field_validator, ValidationInfo
from pydantic import StrictStr, StrictBool, FilePath, DirectoryPath

from .utils import read_yaml, write_yaml


## -- Default directory names ----
class DefaultPaths:
    CONFIG_FILENAME: StrictStr = "mkslides.yml"
    SLIDE_DIR: StrictStr = "slides"
    OUTPUT_DIR: StrictStr = "decks"


## -- Type annotations for MARP Directives ----
class DirectivesConfig:
    THEME = Literal["default", "gaia", "uncover"]
    PAGINATE = StrictBool
    HEADER = Optional[Union[str, None]]
    FOOTER = Optional[Union[str, None]]


class MarpOutputFormats:
    HTML: str = "html"
    PDF: str = "pdf"
    PPTX: str = "pptx"


OutputFormat = Union[str, List[str]]


## -- Configuration class for MkSlides ----
class MkSlidesConfig(BaseModel):
    name: StrictStr
    """Name of slide deck. This will be used to create the (intermediate) markdown and rendered presentation file."""

    description: StrictStr
    """Description of slide deck, target audience, etc. Not currently used in output slide deck."""

    author: StrictStr
    """Author of slide deck/configuration. Not currently used in output slide deck."""

    output_format: OutputFormat = MarpOutputFormats.HTML
    """Output format for deck. Can be a single or list of values. MARP supports HTML (default), PDF, and """

    output_dir: DirectoryPath = DefaultPaths.OUTPUT_DIR

    slide_dir: DirectoryPath = DefaultPaths.SLIDE_DIR
    """Directory containing markdown slide files. Default is 'slides'."""

    slides: List[FilePath]
    """List of filepaths for markdown slides. Needs to include full path to file, including `slide_dir` to pass validation."""

    @field_validator("slides", mode="before")
    def validate_files_exist(cls, field_value, info: ValidationInfo):
        assert info.data is not None
        return [
            os.path.join(info.data.get("slide_dir"), filename)
            for filename in field_value
        ]

    overwrite: StrictBool = False
    """Boolean flag to allow/block overwrite existing slide deck with same name."""

    theme: DirectivesConfig.THEME = "default"
    """MARP theme option. (3) available options, including 'default', 'gaia', and 'uncover'."""

    paginate: DirectivesConfig.PAGINATE = False
    """MARP Directive to apply page numbers to individual slides."""

    header: DirectivesConfig.HEADER = None
    """Optional string to use as header for slides. This is a MARP Directive."""

    footer: DirectivesConfig.FOOTER = None
    """Optional string to use as footer for slides. This is a MARP Directive."""


def load_config(filename: FilePath) -> MkSlidesConfig:
    """Loads YAML configuration file and initializes MkSlides Configuration class."""
    _configs = read_yaml(filename)
    return MkSlidesConfig(**_configs)


def get_default_configuration() -> dict:
    """Returns dictionary of default/vanilla MkSlides configurations."""
    return {
        "name": "my-slide-deck.md",
        "description": "First deck developed by mkslides.",
        "author": "Your name here, please!",
        "output_format": "html",
        "theme": "default",
        "paginate": False,
        "header": None,
        "footer": None,
        "overwrite": True,
        "slides": ["cover.md"],
    }


def initialize_configuration_file() -> None:
    _default_config = get_default_configuration()
    write_yaml(DefaultPaths.CONFIG_FILENAME, _default_config)
    return
