import collections
import math
import sys

def val(d, x):
    try:
        return int(x)
    except ValueError:
        return d[x]

def common_instrs(registers, inst):
    """Evaluates common instructions between parts 1 and 2.
    (set, sub, mul, mod, jnz)

    Returns:
        amount to adjust pc by if there was a jgz that was true
        or otherwise 0
    """
    if inst[0] == "set":
        registers[inst[1]] = val(registers, inst[2])
    elif inst[0] == "sub":
        registers[inst[1]] -= val(registers, inst[2])
    elif inst[0] == "mul":
        registers[inst[1]] *= val(registers, inst[2])
    elif inst[0] == "mod":
        registers[inst[1]] = registers[inst[1]] % val(registers, inst[2])
    elif inst[0] == "jnz":
        if val(registers, inst[1]) != 0:
            return val(registers, inst[2]), 0
    else:
        raise ValueError("Invalid instruction %s" % inst[0])
    return 1, int(inst[0] == "mul")

def part_1(instrs):
    registers = collections.defaultdict(int)
    pc = 0
    num_muls = 0
    while pc < len(instrs):
        inst = instrs[pc]
        pc_delta, mul = common_instrs(registers, inst)
        num_muls += mul
        pc += pc_delta
    return num_muls

def is_prime(n):
    for i in xrange(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True

def part_2():
    start = 100 * 93 + 100000
    end = start + 17000
    compos = 0
    for i in xrange(start, end + 1, 17):
        if not is_prime(i):
            compos+=1
    return compos

if __name__ == "__main__":
    instrs = []
    for l in sys.stdin:
        instrs.append(l.strip().split())
    print part_1(instrs)
    print part_2()
