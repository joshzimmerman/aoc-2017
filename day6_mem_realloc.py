import sys

def part_1(bank):
    visited = list()
    while tuple(bank) not in visited:
        visited.append(tuple(bank))
        maxval = bank[0]
        argmax = 0
        for i in xrange(len(bank)):
            if bank[i] > maxval:
                maxval = bank[i]
                argmax = i
        i = (argmax + 1) % len(bank)
        bank[argmax] = 0
        while maxval > 0:
            bank[i] += 1
            maxval -= 1
            i = (i + 1) % len(bank)
    print len(visited) - visited.index(tuple(bank))
    return len(visited)

if __name__ == "__main__":
    bank = [int(s) for s in sys.argv[1:]]
    print part_1(bank)
