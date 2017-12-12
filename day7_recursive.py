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
    if conflict:
        print children[node]
        for c in children[node]:
            print weights[c]
    weights[node] = tot
    return tot

if __name__ == "__main__":
    pointed_to = []
    progs = []
    weights = {}
    children = {}
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
    calc_weights(root, weights, children)

    for p in progs:
        for child in children[p]:
            if weights[children[p][0]] != weights[child]:
                print "for " + p
                print (child + " wrong weight; should be " + str(weights[children[p][0]]) + 
                       " but is " + str(weights[child]))
