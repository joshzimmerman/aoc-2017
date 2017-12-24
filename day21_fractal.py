import sys

STARTING_BOARD = (".#.", "..#", "###")

def rotate_90(board):
    """e.g.,
    [[a, b],  =>  [[c, a]
     [c, d]]       [d, b]]
    """
    return tuple("".join(r[i] for r in board[::-1]) for i in xrange(len(board)))

def mirror(board):
    """e.g.,
    [[a, b],  =>  [[c, d],
     [c, d]]       [a, b]]
    """
    return tuple(board[::-1])

def rotations(board):
    single_rot = rotate_90(board)
    double_rot = rotate_90(single_rot)
    triple_rot = rotate_90(double_rot)
    boards = set([board, single_rot, double_rot, triple_rot])
    mirrors = set(mirror(b) for b in boards)
    return boards.union(mirrors)

def get_rule(rules, board):
    for r in rotations(board):
        if r in rules:
            return rules[r]
    raise ValueError("%s has no rules" % board)

def split(board):
    """Split a board into 2x2 or 3x3 chunks"""
    out = []
    if len(board) % 2 == 0:
        size = 2
    else:
        assert len(board) % 3 == 0
        size = 3
    row = 0
    while row < len(board):
        elems = [[] for _ in xrange(len(board) / size)]
        for i in xrange(size):
            for j in xrange(len(elems)):
                elems[j].append("".join(board[row + i][j * size:(j + 1) * size]))
        out.append([tuple(e) for e in elems])
        row += size
    return out

def join(split_board):
    """Take a board that was split into 2x2 or 3x3 chunks and merge them"""
    out = []
    for merged_row in split_board:
        for i in xrange(len(merged_row[0])):
            out.append("".join(merged_row[j][i] for j in xrange(len(merged_row))))
    return out

def eval_rule(rules, split_board):
    out = []
    for row in split_board:
        row_out = []
        for mini in row:
            row_out.append(get_rule(rules, mini))
        out.append(row_out)
    return out

def part_1(rules, iterations):
    board = STARTING_BOARD
    for _ in xrange(iterations):
        board = join(eval_rule(rules, split(board)))
    return sum(sum(int(c == '#') for c in r) for r in board)

if __name__ == "__main__":
    rules = {}
    for l in sys.stdin:
        pre, post = l.strip().split(" => ")
        pre = tuple(pre.split("/"))
        post = tuple(post.split("/"))
        rules[pre] = post
    print part_1(rules, 5)
    print part_1(rules, 18)
