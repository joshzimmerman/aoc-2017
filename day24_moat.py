import sys

def optimize(ports, better, match=0):
    frontier = [p for p in ports if match in p]
    best = 0
    best_path = []
    best_len = 0
    for f in frontier:
        if f[0] == match:
            other = f[1]
        else:
            other = f[0]
        weight = f[0] + f[1]
        ports.remove(f)
        path, val = optimize(ports, better, match=other)
        ports.add(f)
        if better(len(path), best_len, val, weight, best):
            best_path = [f] + path
            best = val + weight
            best_len = len(path)
    return best_path, best

def part_1(actual_len, best_len, val, weight, best):
    return val + weight > best

def part_2(actual_len, best_len, val, weight, best):
    return actual_len > best_len or (actual_len == best_len
                                     and val + weight > best)

if __name__ == "__main__":
    ports = set()
    for l in sys.stdin:
        nums = l.split("/")
        ports.add((int(nums[0]), int(nums[1])))
    _, best = optimize(ports, part_1)
    print best
    _, best = optimize(ports, part_2)
    print best
