import sys
INPUT = int(sys.stdin.read())

def list_after(upper):
    l = [0]
    cur_pos = 0
    for i in xrange(1, upper + 1):
        cur_pos = (cur_pos + INPUT) % len(l)
        l = l[:cur_pos + 1] + [i] + l[cur_pos + 1:]
        cur_pos = (cur_pos + 1) % len(l)
    return l, cur_pos

def part_1():
    l, cur_pos = list_after(2017)
    return l[cur_pos + 1]

def part_2():
    after_zero = 0
    cur_pos = 0
    for i in xrange(1, 50000000 + 1):
        size = i
        cur_pos = (cur_pos + INPUT) % size
        if cur_pos == 0:
            after_zero = i
        cur_pos += 1
    return after_zero

if __name__ == "__main__":
    print part_1()
    print part_2()
