import sys

def part_1(path):
    x = 0
    y = path[0].index("|")
    x_change = 1
    y_change = 0
    out_str = ""
    steps = 0
    while path[x][y] != " ":
        if path[x][y].isalpha():
            out_str += path[x][y]
        elif path[x][y] == "+":
            if x_change:
                x_change = 0
                if y + 1 < len(path[x]) and path[x][y + 1] != " ":
                    y_change = 1
                else:
                    y_change = -1
            else:
                y_change = 0
                if (x + 1) < len(path) and path[x + 1][y] != " ":
                    x_change = 1
                else:
                    x_change = -1

        x += x_change
        y += y_change
        steps += 1
    return out_str, steps

if __name__ == "__main__":
    path = []
    for l in sys.stdin:
        path.append(l.strip('\n'))
    print part_1(path)
