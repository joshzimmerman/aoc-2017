import sys

def part_1(insts):
    ip = 0
    steps = 0
    while ip < len(insts):
        new_ip = ip + insts[ip]
        insts[ip] += 1
        ip = new_ip
        steps += 1
    return steps

def part_2(insts):
    ip = 0
    steps = 0
    while ip < len(insts):
        new_ip = ip + insts[ip]
        if insts[ip] >= 3:
            insts[ip] -= 1
        else:
            insts[ip] += 1
        ip = new_ip
        steps += 1
    return steps


if __name__ == "__main__":
    insts = []
    for l in sys.stdin:
        insts.append(int(l.strip()))
    print part_1(insts[:])
    print part_2(insts)
