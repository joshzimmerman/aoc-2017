import sys

def part_1(lines):
    diffs = []
    for l in lines:
        diffs.append(max(l) - min(l))
    return sum(diffs)

def part_2(lines):
    quotients = []
    def line_quotient(l):
        sort = sorted(l)
        for i in xrange(len(l)):
            for j in xrange(i):
                if sort[i] % sort[j] == 0:
                    return sort[i] / sort[j]
    for l in lines:
        quotients.append(line_quotient(l))
    return sum(quotients)

if __name__ == "__main__":
    lines = []
    for l in sys.stdin:
        lines.append([int(s) for s in l.split()])
    print part_1(lines)
    print part_2(lines)
