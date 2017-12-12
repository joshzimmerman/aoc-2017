import sys

def part_1(passphrases):
    def is_valid(p):
        return len(set(p)) == len(p)
    return sum(is_valid(p) for p in passphrases)

def part_2(passphrases):
    sorted_ps = [["".join(sorted(word)) for word in p] for p in passphrases]

    def is_valid(p):
        return len(set(p)) == len(p)
    return sum(is_valid(p) for p in sorted_ps)

if __name__ == "__main__":
    passphrases = []
    for l in sys.stdin:
        passphrases.append(l.split())
    print part_1(passphrases)
    print part_2(passphrases)

