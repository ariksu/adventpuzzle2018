from solutions.tools import open_input
from typing import Tuple, TextIO, Dict


def contain23s(boxname: str) -> Tuple[bool, bool]:
    twos, threes = False, False
    counter = dict()  # type: Dict[str, int]
    for letter in boxname:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    for count in counter.values():
        if count == 2:
            twos = True
        if count == 3:
            threes = True
    return twos, threes


def checksum(file: TextIO) -> int:
    twos, threes = 0, 0
    for boxname in file:
        boxtwos, boxthrees = contain23s(boxname.strip())
        if boxtwos:
            twos += 1
        if boxthrees:
            threes += 1
    return twos * threes


if __name__ == '__main__':
    f = open_input("2")
    print(checksum(f))
