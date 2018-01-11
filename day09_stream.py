import sys

if __name__ == "__main__":
    data = sys.stdin.read()
    num_bracket = 0
    has_angle = False
    score = 0
    i = 0
    garbage = 0
    while i < len(data):
        if data[i] == '!' and has_angle:
            # Skip next
            i += 1
        elif data[i] == '<' and not has_angle:
            has_angle = True
        elif data[i] == '>':
            has_angle = False
        elif has_angle:
            garbage+=1
        elif data[i] == '{' and not has_angle:
            num_bracket += 1
            score += num_bracket
        elif data[i] == '}' and not has_angle:
            num_bracket -= 1
        i += 1
    print score
    print garbage
