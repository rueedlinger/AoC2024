import re


def get_content(path):
    with open(path) as f_input:
        return f_input.read()


def score(text):
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
    result = []

    matches = re.findall(pattern, text)
    enabled = True
    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        else:
            inst = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", match)
            x = int(inst[0][0])
            y = int(inst[0][1])

            if enabled:
                result.append(x * y)

    return sum(result)


def main():
    text = get_content("input/input.txt")
    print(f"score: {score(text)}")


if __name__ == '__main__':
    main()
