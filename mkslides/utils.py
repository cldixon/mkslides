import yaml 
from typing import List

def open_file(fname: str) -> str:
    with open(fname, 'r') as in_file:
        content = in_file.read()
        in_file.close()
    return content

def open_files(fnames: List[str]) -> List[str]:
    return [
        open_file(f) for f in fnames
    ]

def save_to_file(outname: str, content: str) -> None:
    with open(outname, 'w') as out_file:
        out_file.write(content)
        out_file.close()
    return 


def read_yaml(filename: str) -> dict:
    with open(filename, 'r') as in_file:
        data = yaml.safe_load(in_file)
    return data

def write_yaml(filename: str, data: dict) -> None:
    with open(filename, 'w') as out_file:
        yaml.safe_dump(data, out_file)
    return