import re


def get_lines(path):
    with open(path) as f_input:
        return [x.strip() for x in f_input.readlines()]


def create_grid(lines):
    grid = []
    for line in lines:
        row = []
        for character in line:
            row.append(character)
        grid.append(row)
    return grid


def print_grid(grid):
    for row in grid:
        line = ""
        for column in row:
            line += column
        print(line)


def get_vectors(x, y):
    N = [(x, y), (x, y - 1), (x, y - 2), (x, y - 3)]
    S = [(x, y), (x, y + 1), (x, y + 2), (x, y + 3)]
    E = [(x, y), (x + 1, y), (x + 2, y), (x + 3, y)]
    W = [(x, y), (x - 1, y), (x - 2, y), (x - 3, y)]
    NW = [(x, y), (x - 1, y - 1), (x - 2, y - 2), (x - 3, y - 3)]
    SE = [(x, y), (x + 1, y + 1), (x + 2, y + 2), (x + 3, y + 3)]
    NE = [(x, y), (x + 1, y - 1), (x + 2, y - 2), (x + 3, y - 3)]
    SW = [(x, y), (x - 1, y + 1), (x - 2, y + 2), (x - 3, y + 3)]

    return [N, S, E, W, NE, SE, SW, NW]


def is_in_grid(x, y, grid):
    max_y = len(grid) - 1
    min_y = 0
    max_x = len(grid[0]) - 1
    min_x = 0
    return min_x <= x <= max_x and min_y <= y <= max_y


def is_vector_in_grid(coordinates, grid):
    for pos in coordinates:
        if not is_in_grid(pos[0], pos[1], grid):
            return False
    return True


def get_word(vector, grid):
    word = ""
    for pos in vector:
        y = pos[1]
        x = pos[0]
        word += grid[y][x]
    return word


def is_XMAS(word):
    return word == 'XMAS' or word == "SAMX"


def main():
    lines = get_lines("input/input.txt")
    grid = create_grid(lines)
    #print_grid(grid)

    possible_solutions = []
    found = set()

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            vectors = get_vectors(x, y)
            for vector in vectors:
                if is_vector_in_grid(vector, grid):
                    if not str(sorted(vector)) in found:
                        possible_solutions.append(vector)
                        found.add(str(sorted(vector)))

    count = 0

    for solution in possible_solutions:

        if is_XMAS(get_word(solution, grid)):
            count += 1

    print(f"solution: {count}")


if __name__ == '__main__':
    main()
