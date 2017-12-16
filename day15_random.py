INT_MAX = 0x7fffffff
LOW_16_MASK = 0xffff

GEN_A_START = 703
GEN_B_START = 516
NUM_TO_COMPARE = 5000000

def generator(start, mul, mult_of):
    val = start
    while True:
        val = (mul * val) % INT_MAX
        if val % mult_of == 0:
            yield val

if __name__ == "__main__":
    generator_a = generator(GEN_A_START, 16807, 4)
    generator_b = generator(GEN_B_START, 48271, 8)
    same = 0
    for i in xrange(NUM_TO_COMPARE):
        a = next(generator_a)
        b = next(generator_b)
        if (a & LOW_16_MASK) == (b & LOW_16_MASK):
            same += 1
    print same

