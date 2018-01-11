import sys

def calc_weights(node, weights, children):
    tot = weights[node]
    each = None
    conflict = False
    for child in children[node]:
        res = calc_weights(child, weights, children)
        if not each:
            each = res
        tot += res
        if each != res:
            conflict = True
    weights[node] = tot
    return tot

def unbalanced_child(node, weights, children):
    child_weights = {}
    for c in children[node]:
        res = unbalanced_child(c, weights, children)
        if res is not None:
            return res
        w = weights[c]
        if w in child_weights:
            child_weights[w] = None
        else:
            child_weights[w] = c
    if len(child_weights) <= 1:
        return None
    wrong_weight = [w for w in child_weights if child_weights[w] is not None][0]
    right_weight = [w for w in child_weights if child_weights[w] is None][0]
    weight_delta = right_weight - wrong_weight
    return child_weights[wrong_weight], weight_delta


def part_2(root, weights, children):
    orig_weights = weights.copy()
    calc_weights(root, weights, children)
    child, weight_delta = unbalanced_child(root, weights, children)
    return orig_weights[child] + weight_delta

if __name__ == "__main__":
    pointed_to = []
    progs = []
    weights = {}
    children = {}  # Map program to its children
    for l in sys.stdin:
        prog = l.split()[0]
        progs.append(prog)
        weights[prog] = int(l[l.index("(") + 1:l.index(")")])
        if "->" in l:
            pointees = [s.strip() for s in l[l.index(">")+1:].split(",")]
            pointed_to.extend(pointees)
            children[prog] = pointees
        else:
            children[prog] = []


    root = [p for p in progs if p not in pointed_to][0]
    print root
    print part_2(root, weights, children)
