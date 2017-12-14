import sys
import day10_hashing

def count_ones(h):
    return sum(1 if c == '1' else 0 for c in h)

def neighbors(hashes, (a,b)):
    neighbors = []
    if a > 0:
        neighbors.append((a - 1, b))
    if b > 0:
        neighbors.append((a, b - 1))
    if a < len(hashes) - 1:
        neighbors.append((a + 1, b))
    if b < len(hashes[0]) - 1:
        neighbors.append((a, b + 1))
    return [(a,b) for (a,b) in neighbors if hashes[a][b] == '1']

def reachable(hashes, start=(0,0), visited=None):
    if visited is None:
        visited = set()
    if start in visited:
        return set()
    visited.add(start)
    reached = set()
    for neighbor in neighbors(hashes, start):
        new_reached = reachable(hashes, start=neighbor, visited=visited)
        reached = reached | new_reached
    reached.add(start)
    return reached

def part_2(hashes):
    components = 0
    a, b = (0, 0)
    while a < len(hashes):
        if hashes[a][b] == '1':
            group = reachable(hashes, start=(a,b))
            components += 1
            for (x, y) in group:
                hashes[x][y] = '0'
        b = (b + 1) % len(hashes[0])
        if b == 0:
            a += 1
    return components


if __name__ == "__main__":
    inp = sys.argv[1]
    hashes = []
    for i in xrange(128):
        hashes.append(list("{:0128b}".format(int(day10_hashing.compute_hash("%s-%d" % (inp, i)), 16))))
    ones = sum(count_ones(h) for h in hashes)
    print ones
    print part_2(hashes)
