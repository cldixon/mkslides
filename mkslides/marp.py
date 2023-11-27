import subprocess
from typing import List, Literal

from .config import MarpOutputFormats

SLIDE_SEP = "---"
ALLOW_LOCAL_ACCESS: str = "--allow-local-access"


def compile_directives(
    theme: str = "default",
    paginate: bool = False,
    header: str = None,
    footer: str = None,
) -> str:
    # add theme
    directives = [f"theme: {theme}"]
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


def run_marp(filepath: str, output_format: Literal["html", "pdf", "pptx"]) -> None:
    """Run MARP as Python subprocess, with provided filename."""
    _command = ["marp", filepath]
    if output_format == MarpOutputFormats.PDF:
        _command.extend(["--pdf", ALLOW_LOCAL_ACCESS])
    elif output_format == MarpOutputFormats.PPTX:
        _command.extend(["--pptx", ALLOW_LOCAL_ACCESS])
    else:
        pass
    _ = subprocess.run(_command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return
