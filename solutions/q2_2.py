from typing import TextIO, Tuple, Sequence

from solutions.tools import open_input


def boxname_differs(fst: str, snd: str) -> int:
    counter = 0
    for l1, l2 in zip(fst, snd):
        if l1 != l2:
            counter += 1
    return counter


def find_similarish(f: Sequence[str]) -> Tuple[str, str]:
    for i in f:
        for j in f:
            if boxname_differs(i.strip(), j.strip()) == 1:
                return i.strip(), j.strip()
    raise KeyError("no similarish strings found")


if __name__ == '__main__':
    f = open_input("2")
    strings = f.readlines()
    a, b = find_similarish(strings)
    common = [i for i, j in zip(a, b) if i == j]
    print(''.join(common))
