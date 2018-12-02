import os
from typing import Optional, TextIO

here = lambda x: os.path.abspath(os.path.join(os.path.dirname(__file__), x))
INPUTS = here('inputs')


def open_input(name: str) -> TextIO:
    if "." not in name:
        name += ".input"
    try:
        file = open(os.path.join(INPUTS, name))
        return file
    except Exception as e:
        raise e
        return None
