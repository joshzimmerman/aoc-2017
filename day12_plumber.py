import sys

def reachable(d, start=0, visited=None):
    if visited is None:
        visited = set()
    if start in visited:
        return 0, set()
    visited.add(start)
    size = 0
    reached = set()
    for neighbor in d[start]:
        low_size, new_reached = reachable(d, start=neighbor, visited=visited)
        reached = reached | new_reached
        size += low_size
    reached.add(start)
    return 1 + size, reached

def part_2(d):
    components = 0
    while len(d) > 0:
        _, group = reachable(d, start=d.keys()[0])
        components += 1
        for x in group:
            del d[x]
    return components

if __name__ == "__main__":
    d = {}
    for l in sys.stdin:
        split = l.split()
        key = int(split[0])
        vals = []
        for val in split[2:]:
            vals.append(int(val.replace(",","")))
        d[key] = vals
    print reachable(d)
    print part_2(d)
