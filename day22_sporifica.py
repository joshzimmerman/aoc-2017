import sys

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ITERATIONS = 10000

def tuple_add((a,b), (c,d)):
    return (a + c, b + d)

def burst(board, cur, face):
    if cur in board:
        # Turn right
        face = (face + 1) % len(DIRECTIONS)
        board.remove(cur)
        infected = False
    else:
        face = (face - 1) % len(DIRECTIONS)
        board.add(cur)
        infected = True
    return board, tuple_add(cur, DIRECTIONS[face]), face, infected


def part_1(board, cur):
    infecting_bursts = 0
    face = 0
    for i in xrange(ITERATIONS):
        board, cur, face, infected = burst(board, cur, face)
        infecting_bursts += int(infected)
    return infecting_bursts

if __name__ == "__main__":
    row = 0
    cols = 0
    board = set()
    for l in sys.stdin:
        cols = len(l.strip())
        for j in xrange(len(l)):
            if l[j] == "#":
                board.add((row, j))
        row += 1
    cur = (row / 2, cols / 2)
    print part_1(board, cur)
