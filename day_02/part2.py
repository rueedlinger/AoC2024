def get_lines(path):
    with open(path) as f_input:
        return [x.strip() for x in f_input.readlines()]


def clean(lines, sep, f):
    return [[f(y) for y in x.split(sep)] for x in lines]


def is_clean(line):
    diffs = []
    for i, x in enumerate(line):
        if i < len(line) - 1:
            diffs.append(x - line[i + 1])

    inc = all([n < 0 for n in diffs])
    dec = all([n > 0 for n in diffs])
    if inc and min(diffs) > -4:
        # print(line, diffs, max(diffs), min(diffs))
        return True

    if dec and max(diffs) < 4:
        # print(line, diffs, max(diffs), min(diffs))
        return True

    return False


def score(lines):
    safe = []

    for line in lines:
        if is_clean(line):
            safe.append(1)
        else:
            for i in range(len(line)):
                if is_clean(line[:i] + line[i + 1:]):
                    safe.append(1)
                    break

    return sum(safe)


def main():
    lines = get_lines("input/input.txt")
    lines = clean(lines, ' ', lambda x: int(x))

    print(f"lines: {len(lines)}")
    print(f"score: {score(lines)}")


if __name__ == '__main__':
    main()
