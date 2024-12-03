def get_lines(path):
    with open(path) as f_input:
        return [x.strip() for x in f_input.readlines()]


def clean(lines, sep, f):
    return [[f(y) for y in x.split(sep)] for x in lines]


def score(lines):
    safe = []

    for line in lines:
        inc_or_dec = str(sorted(line, reverse=False)) == str(line) or str(sorted(line, reverse=True)) == str(line)
        if inc_or_dec:
            diffs = []
            for i, x in enumerate(line):
                if i < len(line) - 1:
                    diffs.append(abs(x - line[i+1]))
            diffs = sorted(diffs)
            min_diff = min(diffs)
            max_diff = max(diffs)
            if min_diff in [1, 2, 3] and max_diff in [1, 2, 3]:
                safe.append(1)
            else:
                safe.append(0)
        else:
            safe.append(0)


    return sum(safe)



def main():
    lines = get_lines("input/input.txt")
    lines = clean(lines, ' ', lambda x: int(x))

    print(f"lines: {len(lines)}")
    print(score(lines))


if __name__ == '__main__':
    main()
