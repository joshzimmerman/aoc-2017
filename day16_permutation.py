import sys

BILLION = 1000000000

def part_1(progs, moves):
    for m in moves:
        if m[0] == 's':
            shift = int(m[1:])
            progs = progs[-shift:] + progs[0:-shift]
        elif m[0] == 'x':
            a = int(m[1:m.index("/")])
            b = int(m[m.index("/") + 1:])
            tmp = progs[a]
            progs[a] = progs[b]
            progs[b] = tmp
        elif m[0] == 'p':
            p1 = m[1:m.index("/")]
            p2 = m[m.index("/") + 1:]
            p1_idx = progs.index(p1)
            p2_idx = progs.index(p2)
            progs[p1_idx] = p2
            progs[p2_idx] = p1
    return progs

def part_2(progs, move):
    visited = set()
    visited.add("".join(progs))
    permutations = ["".join(progs)]
    for i in xrange(BILLION):
        progs = part_1(progs, moves)
        s = "".join(progs)
        if s in visited:
            break
        permutations.append(s)
        visited.add(s)

    return permutations[BILLION % len(visited)]

if __name__ == "__main__":
    start_pos = [chr(ord("a") + i) for i in xrange(16)]

    moves = []
    for l in sys.stdin:
        moves.extend(l.strip().split(','))
    print "".join(part_1(start_pos[:], moves))
    print part_2(start_pos, moves)
