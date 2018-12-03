from typing import TextIO, Sequence, Tuple, Optional

from solutions.tools import open_input
from pprint import pprint


class Claims(object):
    claims = dict()
    storage = dict()
    intersections = None

    def __init__(self, f: Sequence[str]) -> None:

        self.Load(f)
        self.Parse()
        print(min(self.storage), ' ', max(self.storage))
        pass

    def Load(self, f: TextIO) -> None:
        for i, line in enumerate(f):
            claim_id, claim = line.strip().split('@')
            start, size = claim.strip().split(':')
            coords = list(start.strip().split(','))
            assert len(coords) == 2
            sizes = list(size.strip().split('x'))
            assert len(sizes) == 2
            self.claims[int(claim_id.strip('# '))] = dict(xy=coords, dxdy=sizes)
        pass

    def Parse(self) -> None:
        for i in range(1000):
            self.storage[i] = dict()
            for j in range(1000):
                self.storage[i][j] = list()
        for claimid, claim in self.claims.items():
            x, y = claim['xy']
            dx, dy = claim['dxdy']
            for x, y in coords_gen(int(x), int(y), int(dx), int(dy)):
                self.storage[x][y].append(claimid)
        pass

    def Count_Intesections(self) -> int:
        if self.intersections is not None:
            return self.intersections
        self.intersections = 0
        for i in range(1000):
            for j in range(1000):
                if len(self.storage[i][j]) > 1:
                    self.intersections += 1
        return self.intersections

    def find_clean_cut(self) -> Optional[int]:
        clean = {i: True for i in range(1, max(self.claims) + 1)}
        for i in range(1000):
            for j in range(1000):
                if len(self.storage[i][j]) > 1:
                    for claimid in self.storage[i][j]:
                        clean[claimid]=False
        for claimid in clean:
            if clean[claimid]:
                return claimid


def coords_gen(x: int, y: int, dx: int, dy: int) -> Sequence[Tuple[int, int]]:
    for i in range(x, x + dx):
        for j in range(y, y + dy):
            yield (i, j)


if __name__ == '__main__':
    f = list()
    for line in open_input("3"):
        f.append(line.strip())
    x = Claims(f)
    print(x.Count_Intesections())
    print(x.find_clean_cut())
