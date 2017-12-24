import collections
import sys

SIMPLIFIERS = {"n": {"se": "ne", "sw": "nw"},
               "ne": {"s": "se", "nw": "n"},
               "se" : {"n": "ne", "sw": "s"},
               "s": {"ne": "se", "nw": "sw"},
               "sw": {"n": "nw", "se": "s"},
               "nw": {"ne": "n", "s": "sw"}}

def simplify(d):
    OPPS = [('n', 's'), ('ne', 'sw'), ('nw', 'se')]
    for a, b in OPPS:
        if d[a] > d[b]:
            d[a] -= d[b]
            d[b] = 0
        else:
            d[b] -= d[a]
            d[a] = 0
    for step in SIMPLIFIERS:
        if d[step] > 0:
            for other in SIMPLIFIERS[step]:
                simp_count = min(d[step], d[other])
                d[step] -= simp_count
                d[other] -= simp_count
                d[SIMPLIFIERS[step][other]] += simp_count
    return d

def part_1(path):
    d = collections.defaultdict(int)
    highest = 0
    for step in path:
        d[step] += 1
        simplify(d)
        if sum(d.values()) > highest:
            highest = sum(d.values())
    simplify(d)
    return sum(d.values()), highest

if __name__ == "__main__":
    path = sys.stdin.readline().strip().split(",")
    print part_1(path)
