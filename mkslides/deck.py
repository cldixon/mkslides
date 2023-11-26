import os 
from typing import List, Literal, Union
from dataclasses import dataclass, asdict
from .utils import open_files, save_to_file
from .config import MkSlidesConfig, OutputFormat
from .marp import compile_directives, compile_slides, run_marp

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
        self.output_format: OutputFormat = config.output_format
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
            os.path.join(self.output_dir, self.name), self.content
        )

    def convert_with_marp(self):
        source_md_file = os.path.join(self.output_dir, self.name)
        if isinstance(self.output_format, str):
            run_marp(source_md_file, output_format=self.output_format)
        else:
            [run_marp(source_md_file, output_format=_format) for _format in self.output_format]
        return 

    def build(self) -> None:
        self.assemble_slides()
        self.save_markdown_slides()
        self.convert_with_marp()
        return 