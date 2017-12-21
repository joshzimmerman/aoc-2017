import collections
import re
import sys

POINT = "<(-?\d+),(-?\d+),(-?\d+)>"
LINE_RE = re.compile("p=%s, v=%s, a=%s" % (POINT, POINT, POINT))

def step(particles, steps=1):
    i = 0
    while i < len(particles):
        ((px, py, pz), (vx, vy, vz), (ax, ay, az)) = particles[i]
        vx += ax
        vy += ay
        vz += az

        px += vx
        py += vy
        pz += vz
        particles[i] = ((px, py, pz), (vx, vy, vz), (ax, ay, az))
        i += 1

def part_1(particles):
    min_acc = None
    min_idx = []
    i = 0
    for (p, v, a) in particles:
        acc = abs(a[0]) + abs(a[1]) + abs(a[2])
        if min_acc is None or acc <= min_acc:
            min_acc = acc
            min_idx.append(i)
        i += 1

    min_v = None
    min_v_idx = None
    for i in min_idx:
        (_, v, _) = particles[i]
        vel = abs(v[0]) + abs(v[1]) + abs(v[2])
        if min_v is None or vel < min_v:
            min_v = v
            min_v_idx = i
    return min_v_idx

def part_2(particles):
    last_len = len(particles)
    stable_iters = 0
    while stable_iters < 20:
        d = collections.defaultdict(list)
        for i, (p,_,_) in enumerate(particles):
            d[p].append(i)
        for k, v in d.iteritems():
            if len(v) > 1:
                deleted = 0
                for i in v:
                    particles[i] = particles[-1 - deleted]
                    deleted += 1
                particles = particles[:- deleted]

        if last_len != len(particles):
            stable_iters = 0
            last_len = len(particles)
        else:
            stable_iters += 1
        step(particles)
    return len(particles)


if __name__ == "__main__":
    particles = []
    for l in sys.stdin:
        match = LINE_RE.match(l)
        p = (int(match.group(1)), int(match.group(2)), int(match.group(3)))
        v = (int(match.group(4)), int(match.group(5)), int(match.group(6)))
        a = (int(match.group(7)), int(match.group(8)), int(match.group(9)))
        particles.append((p, v, a))
    print part_1(particles)
    print part_2(particles)
