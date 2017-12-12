import collections
import sys
if __name__ == "__main__":
    l = []
    regs = collections.defaultdict(int)
    max_tot = 0
    for l in sys.stdin:
        parts = l.split()
        reg = parts[0]
        delta = int(parts[2])
        if parts[1] == 'dec':
            delta = -delta
        comp_reg = parts[4]
        operator = parts[5]
        comp_imm = int(parts[6])
        if ((operator == '==' and regs[comp_reg] == comp_imm) or
            (operator == '>' and regs[comp_reg] > comp_imm) or
            (operator == '<' and regs[comp_reg] < comp_imm) or
            (operator == '>=' and regs[comp_reg] >= comp_imm) or
            (operator == '<=' and regs[comp_reg] <= comp_imm) or
            (operator == '!=' and regs[comp_reg] != comp_imm)):
            regs[reg] += delta
            if regs[reg] > max_tot:
                max_tot = regs[reg]
    print max(regs.values())
    print max_tot
