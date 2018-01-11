import collections
import sys

def sum_pair(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def make_dict(upper):
    d = {}
    values = collections.defaultdict(int)
    reverse_d = {}
    directions = ['right', 'up', 'left', 'down']
    dir_deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # Base cases
    d[(0, 0)] = 1
    d[(0, 1)] = 2
    values[(0, 0)] = 1
    values[(0, 1)] = 1
    first_above_upper = None

    dir_idx = 1
    i = 3
    cur_coord = (0, 1)
    while i <= upper:
        possible_next = dir_deltas[(dir_idx + 1) % len(dir_deltas)]
        if sum_pair(possible_next, cur_coord) not in d:
            cur_coord = sum_pair(possible_next, cur_coord)
            dir_idx = (dir_idx + 1) % len(dir_deltas)
        else:
            cur_coord = sum_pair(dir_deltas[dir_idx], cur_coord)
        d[cur_coord] = i
        reverse_d[i] = cur_coord
        val = 0
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                val += values[sum_pair((x,y),cur_coord)]
        values[cur_coord] = val
        if val > upper and first_above_upper is None:
            first_above_upper = val
        i += 1

    return reverse_d, first_above_upper

def part_1(num, reverse_d):
    coord = reverse[num]
    return abs(coord[0]) + abs(coord[1])


if __name__ == "__main__":
    num = int(sys.stdin.readline())
    reverse, first_above_upper = make_dict(num)
    print part_1(num, reverse)
    print first_above_upper

