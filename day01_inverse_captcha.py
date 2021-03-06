import sys
def part_one(digits):
    tot = 0
    for i in xrange(len(digits)):
        if digits[i] == digits[i - 1]:
            tot += int(digits[i])
    return tot

def part_two(digits):
    tot = 0
    for i in xrange(len(digits)):
        if digits[i] == digits[(i + len(digits) / 2) % len(digits)]:
            tot += int(digits[i])
    return tot
if __name__ == "__main__":
    num = sys.stdin.readline().strip()
    print part_one(num)
    print part_two(num)
