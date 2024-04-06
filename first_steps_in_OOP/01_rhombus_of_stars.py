n = int(input())


def print_row(row):
    print(" " * (n - row), " *" * row)


def create_upper_part_rhombus():
    for row in range(1, n + 1):
        print_row(row)


def create_bottom_part_rhombus():
    for row in range(n - 1, 0, -1):
        print_row(row)


create_upper_part_rhombus()
create_bottom_part_rhombus()
