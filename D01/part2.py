def get_lines(path):
    with open(path) as f_input:
        return [x.strip() for x in f_input.readlines()]


def clean(lines, sep, f):
    return [[f(y) for y in x.split(sep)] for x in lines]


def get_pairs(lines):
    xs = []
    ys = []
    for x in lines:
        xs.append(x[0])
    for y in lines:
        ys.append(y[1])

    return xs, ys


def score(xs, ys):
    result = []
    for x in xs:
        c = ys.count(x)
        result.append(c * x)
    return sum(result)


def main():
    lines = get_lines("input/input.txt")
    lines = clean(lines, '   ', lambda x: int(x))

    print(f"lines: {len(lines)}")
    xs, ys = get_pairs(lines)
    print(f"score: {score(xs, ys)}")


if __name__ == '__main__':
    main()
