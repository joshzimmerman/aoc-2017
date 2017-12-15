import sys

def part_1(d):
    return sum(k * v for k, v in d.iteritems() if k % ((v - 1) * 2) == 0)

def part_2(d):
    delay = 0
    valid = False
    while not valid:
        delay += 1
        valid = valid or not(any((k + delay) % ((v - 1) * 2) == 0 for k, v in d.iteritems()))
    return delay

if __name__ == "__main__":
    d = {}
    for l in sys.stdin:
        key,val = l.replace(" ", "").split(":")
        d[int(key)] = int(val)
    print part_1(d)
    print part_2(d) 
