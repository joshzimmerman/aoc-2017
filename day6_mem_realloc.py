import sys

def redistribute(bank):
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
    return len(visited), len(visited) - visited.index(tuple(bank))

if __name__ == "__main__":
    args = sys.stdin.read().split()
    bank = [int(s) for s in args]
    pt1, pt2 = redistribute(bank)
    print pt1
    print pt2
