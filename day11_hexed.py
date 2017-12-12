import sys


# order irrelevant
# anything twice can't be reduced
# n sw = nw
# n se = ne
# nw s = sw
# nw ne = n
# sw se = s
# sw n = nw
# s nw = sw
# s ne = se
# se n = ne

OPPOSITES = {"n": "s", "ne": "sw", "nw": "se",
             "s": "n", "sw": "ne", "se": "nw"}
SIMPLIFIERS = {"n": {"se": "ne", "sw": "nw"},
               "ne": {"s": "se", "nw": "n"},
               "se" : {"n": "ne", "sw": "s"},
               "s": {"ne": "se", "nw": "sw"},
               "sw": {"n": "nw", "se": "s"},
               "nw": {"ne": "n", "s": "sw"}}

def excise_opposites(path):
    i = 0
    while i < len(path):
        opp = OPPOSITES[path[i]]
        try:
            opp_idx = path.index(opp, i)
            path = path[:i] + path[i + 1:opp_idx] + path[opp_idx + 1:]
        except ValueError:
            i += 1
    return path

def simplify_sequences(path):
    i = 0
    while i < len(path):
        simps = SIMPLIFIERS[path[i]]
        for s in simps:
            try:
                idx = path.index(s, i)
                replace = simps[path[idx]]
                path = path[:i] + path[i + 1:idx] + [replace] + path[idx + 1:]
                break
            except ValueError:
                continue
        else:
            i += 1
    return path

def part_1(path):
    path = excise_opposites(path)
    path = simplify_sequences(path)
    return path

def part_2(path):
    i = 0
    large = 0
    mid = path
    while i < len(path):
        mid = part_1(path[:i])
        if len(mid) > large:
            large = len(mid)
        path = mid + path[i:]
        i = len(mid) + 1
    return large

if __name__ == "__main__":
    path = sys.argv[1].split(",")
    print len(part_1(path))
    print part_2(path)
    print len(path)
