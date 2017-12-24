import sys
INT_MAX = 0x7fffffff
LOW_16_MASK = 0xffff

NUM_TO_COMPARE = 5000000

def generator(start, mul, mult_of):
    val = start
    while True:
        val = (mul * val) % INT_MAX
        if val % mult_of == 0:
            yield val

def compare(num_to_compare, a_mul=1, b_mul=1):
    generator_a = generator(GEN_A_START, 16807, a_mul)
    generator_b = generator(GEN_B_START, 48271, b_mul)
    same = 0
    for i in xrange(num_to_compare):
        a = next(generator_a)
        b = next(generator_b)
        if (a & LOW_16_MASK) == (b & LOW_16_MASK):
            same += 1
    return same

if __name__ == "__main__":
    GEN_A_START = int(sys.stdin.readline().split()[-1])
    GEN_B_START = int(sys.stdin.readline().split()[-1])
    print compare(40000000)
    print compare(5000000, a_mul=4, b_mul=8)

