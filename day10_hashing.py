import sys
ALWAYS_ADD = [17, 31, 73, 47, 23]
def reverse(l, start, length):
    i = start
    j = (start + length - 1) % len(l)
    flipped = 0
    while flipped < length:
        tmp = l[i]
        l[i] = l[j]
        l[j] = tmp
        i = (i + 1) % len(l)
        j = (j - 1) % len(l)
        flipped += 2

def hash_round(lengths, l, cur_pos, skip):
    for length in lengths:
        reverse(l, cur_pos, length)
        cur_pos = (cur_pos + length + skip) % len(l)
        skip += 1
    return l, cur_pos, skip

if __name__ == "__main__":
    lengths = [ord(x) for x in sys.argv[1]] + ALWAYS_ADD
    cur_pos = 0
    skip = 0
    l = range(256)
    for _ in xrange(64):
        l, cur_pos, skip = hash_round(lengths, l, cur_pos, skip)
    dense = []
    i = 0
    while i < len(l):
        xor = 0
        for j in xrange(16):
            xor = xor ^ l[i + j]
        i += 16
        dense.append(xor)

    hash_str = "".join("{:02x}".format(x) for x in dense)
    print hash_str

