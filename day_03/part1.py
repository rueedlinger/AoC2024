import re


def get_lines(path):
    with open(path) as f_input:
        return [x.strip() for x in f_input.readlines()]


def get_matches(lines):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = []
    for line in lines:
        match = re.findall(pattern, line)
        if len(match) > 0:
            matches.append(match)
    return matches


def score(matches):
    r = []
    for match in matches:
        for x, y in match:
            r.append(int(x) * int(y))
    return sum(r)


def main():
    lines = get_lines("input/input.txt")
    print(f"lines: {len(lines)}")
    print(f"score: {score(get_matches(lines))}")


if __name__ == '__main__':
    main()
