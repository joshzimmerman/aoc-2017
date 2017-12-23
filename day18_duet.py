import collections
import sys

def val(d, x):
    try:
        return int(x)
    except ValueError:
        return d[x]

def common_instrs(registers, inst):
    """Evaluates common instructions between parts 1 and 2.
    (set, add, mul, mod, jgz)

    Returns:
        amount to adjust pc by if there was a jgz that was true
        or otherwise 0
    """
    if inst[0] == "set":
        registers[inst[1]] = val(registers, inst[2])
    elif inst[0] == "add":
        registers[inst[1]] += val(registers, inst[2])
    elif inst[0] == "mul":
        registers[inst[1]] *= val(registers, inst[2])
    elif inst[0] == "mod":
        registers[inst[1]] = registers[inst[1]] % val(registers, inst[2])
    elif inst[0] == "jgz":
        if val(registers, inst[1]) > 0:
            return val(registers, inst[2])
    else:
        raise ValueError("Invalid instruction %s" % inst[0])
    return 0

def part_1(instrs):
    registers = collections.defaultdict(int)
    last_sound = None
    first_rcv = None
    pc = 0
    while pc < len(instrs):
        inst = instrs[pc]
        if inst[0] == "snd":
            last_sound = val(registers, inst[1])
        elif inst[0] == "rcv":
            if first_rcv is None and val(registers, inst[1]) != 0:
                return last_sound
        else:
            jgz_delta = common_instrs(registers, inst)
            if jgz_delta != 0:
                pc += jgz_delta
                continue
        pc += 1
    return first_rcv

def part_2(instrs):
    contexts = [collections.defaultdict(int),
                collections.defaultdict(int)]
    pcs = [0, 0]
    channels = [[], []]
    prog = 0
    contexts[0]['p'] = 0
    contexts[1]['p'] = 1
    prog_1_sends = 0
    while pcs[0] < len(instrs) or pcs[1] < len(instrs):
        if (all(not c for c in channels) and
            all(instrs[pc][0] == "rcv" for pc in pcs)):
            print "Deadlock detected"
            break
        inst = instrs[pcs[prog]]
        if inst[0] == "snd":
            channels[1 - prog].append(val(contexts[prog], inst[1]))
            if prog == 1:
                prog_1_sends += 1
        elif inst[0] == "rcv":
            if channels[prog]:
                contexts[prog][inst[1]] = channels[prog].pop(0)
            else:
                # "block" at this instruction waiting for other prog to send.
                prog = 1 - prog
                continue
        else:
            jgz_delta = common_instrs(contexts[prog], inst)
            if jgz_delta != 0:
                pcs[prog] += jgz_delta
                continue
        pcs[prog] += 1

    return prog_1_sends


if __name__ == "__main__":
    instrs = []
    for l in sys.stdin:
        instrs.append(l.strip().split())
    print part_1(instrs)
    print part_2(instrs)
