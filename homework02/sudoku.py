import pathlib
import typing as tp
import random

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:

    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:

    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "")
                for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:

    groups = [values[n * i : n * i + n] for i in range(n)]
    return groups


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:

    return grid[pos[0]]


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:

    x = []
    for i in range(len(grid)):
        x += grid[i][pos[1]]
    return x


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos

    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    Xblock = 3 * (pos[0] // 3)
    Yblock = 3 * (pos[1] // 3)
    return [
        grid[x][y] for x in range(Xblock, Xblock + 3) for y in range(Yblock, Yblock + 3)
    ]


def find_empty_positions(
    grid: tp.List[tp.List[str]],
) -> tp.Optional[tp.Tuple[int, int]]:

    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == ".":
                return (row, col)
    return None


def find_possible_values(
    grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]
) -> tp.Set[str]:

    possible_numbers = set("123456789")
    row_numbers = set(get_row(grid, pos))
    col_numbers = set(get_col(grid, pos))
    block_numbers = set(get_block(grid, pos))
    result = possible_numbers - row_numbers - col_numbers - block_numbers
    return result


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:

    pos = find_empty_positions(grid)

    if not pos:
        return grid
    values = find_possible_values(grid, pos)
    for value in values:
        grid[pos[0]][pos[1]] = value
        solution = []
        solution = solve(grid)
        if solution:
            return solution

    grid[pos[0]][pos[1]] = "."
    return None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:

    for row in range(len(solution)):
        result = set(get_row(solution, (row, 0)))
        if result != set("123456789"):
            return False

    for col in range(len(solution)):
        result = set(get_col(solution, (0, col)))
        if result != set("123456789"):
            return False

    for row in range(0, (len(solution) - 1), 3):
        for col in range(0, (len(solution) - 1), 3):
            result = set(get_block(solution, (row, col)))
            if result != set("123456789"):
                return False

    return True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:

    grid = [["." for _ in range(9)] for _ in range(9)]
    grid = solve(grid)

    cells_hidden = 0
    while N + cells_hidden < 81:
        rnd_row = random.randint(0, 8)
        rnd_col = random.randint(0, 8)
        if grid[rnd_row][rnd_col] != ".":
            grid[rnd_row][rnd_col] = "."
            cells_hidden += 1
    return grid


if __name__ == "__main__":
    for fname in ["puzzle1.txt", "puzzle2.txt", "puzzle3.txt"]:
        grid = read_sudoku(fname)
        display(grid)
        solution = solve(grid)
        if not solution:
            print(f"Puzzle {fname} can't be solved")
        else:
            display(solution)
