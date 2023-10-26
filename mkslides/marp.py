import subprocess
from typing import Literal 

from .config import MarpOutputFormats

ALLOW_LOCAL_ACCESS: str = "--allow-local-access"

def run_marp(filepath: str, output_format: Literal["html", "pdf", "pptx"]) -> None:
    """Run MARP as Python subprocess, with provided filename."""
    _command = ["marp", filepath]
    if output_format == MarpOutputFormats.PDF:
        _command.extend(["--pdf", ALLOW_LOCAL_ACCESS])
    elif output_format == MarpOutputFormats.PPTX:
        _command.extend(["--pptx", ALLOW_LOCAL_ACCESS])
    else:
        pass
    _ = subprocess.run(
        _command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.STDOUT
    )
    return