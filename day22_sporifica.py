import collections
import sys

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
STATES = [".", "W", "#", "F"]
ITERATIONS = 10000

def tuple_add((a,b), (c,d)):
    return (a + c, b + d)

def burst(board, cur, face, state_step_size):
    state = board[cur]
    if state == ".":
        # Turn left
        face = (face - 1) % len(DIRECTIONS)
    elif state == "#":
        # Turn right
        face = (face + 1) % len(DIRECTIONS)
    elif state == "F":
        # Turn around
        face = (face + 2) % len(DIRECTIONS)

    board[cur] = STATES[(STATES.index(state) + state_step_size) % len(STATES)]
    return board, tuple_add(cur, DIRECTIONS[face]), face, board[cur] == "#"

def part_1(board, cur, state_step_size=2, iters=ITERATIONS):
    infecting_bursts = 0
    face = 0
    for i in xrange(iters):
        board, cur, face, infected = burst(board, cur, face, state_step_size)
        infecting_bursts += int(infected)
    return infecting_bursts

def part_2(board, cur):
    return part_1(board, cur, state_step_size=1, iters=10000000)

if __name__ == "__main__":
    row = 0
    cols = 0
    board = collections.defaultdict(lambda: ".")
    for l in sys.stdin:
        if not cols:
            cols = len(l.strip())
        for j in xrange(cols):
            board[(row, j)] = l[j]
        row += 1

    cur = (row / 2, cols / 2)
    print part_1(board.copy(), cur)
    print part_2(board, cur)
