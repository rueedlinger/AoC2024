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


def get_points(x, y):
    UL = (x - 1, y - 1)
    UR = (x + 1, y - 1)
    DL = (x - 1, y + 1)
    DR = (x + 1, y + 1)
    M = (x, y)
    return [UL, UR, DL, DR, M]


def is_in_grid(x, y, grid):
    max_y = len(grid) - 1
    min_y = 0
    max_x = len(grid[0]) - 1
    min_x = 0
    return min_x <= x <= max_x and min_y <= y <= max_y


def are_points_in_grid(points, grid):
    for pos in points:
        if not is_in_grid(pos[0], pos[1], grid):
            return False
    return True


def is_XMAS(x, y, grid):
    dl = [(x - 1, y - 1), (x, y), (x + 1, y + 1)]
    dr = [(x + 1, y - 1), (x, y), (x - 1, y + 1)]
    w1 = ""
    w2 = ""
    for p in dl:
        x = p[0]
        y = p[1]
        w1 += grid[y][x]
    for p in dr:
        x = p[0]
        y = p[1]
        w2 += grid[y][x]
    return (w1 == "MAS" or w1 == "SAM") and (w2 == "MAS" or w2 == "SAM")


def main():
    lines = get_lines("input/input.txt")
    grid = create_grid(lines)
    # print_grid(grid)
    count = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            points = get_points(x, y)
            if are_points_in_grid(points, grid):
                if is_XMAS(x, y, grid):
                    count += 1

    print(f"solution: {count}")


if __name__ == '__main__':
    main()
