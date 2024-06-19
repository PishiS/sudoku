def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))

def find_empty_location(grid):
    min_possibilities = 10  # More than any possible number of possibilities (1-9)
    best_cell = None
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                num_possibilities = sum(check_location_is_safe(grid, row, col, num) for num in range(1, 10))
                if num_possibilities < min_possibilities:
                    min_possibilities = num_possibilities
                    best_cell = (row, col)
    return best_cell

def used_in_row(grid, row, num):
    return any(grid[row][col] == num for col in range(9))

def used_in_col(grid, col, num):
    return any(grid[row][col] == num for row in range(9))

def used_in_box(grid, row, col, num):
    box_start_row, box_start_col = row - row % 3, col - col % 3
    return any(grid[i][j] == num for i in range(box_start_row, box_start_row + 3) for j in range(box_start_col, box_start_col + 3))

def check_location_is_safe(grid, row, col, num):
    return not used_in_row(grid, row, num) and \
           not used_in_col(grid, col, num) and \
           not used_in_box(grid, row, col, num)

def solve_sudoku(grid):
    empty_location = find_empty_location(grid)
    if not empty_location:
        return True  # No empty location means the puzzle is solved

    row, col = empty_location

    for num in range(1, 10):
        if check_location_is_safe(grid, row, col, num):
            grid[row][col] = num

            if solve_sudoku(grid):
                return True

            grid[row][col] = 0  # Reset cell for backtracking

    return False

# Example grid with 0 representing empty cells
sudoku_grid = [
    [3, 0, 0, 0, 5, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 7, 8, 0],
    [0, 6, 9, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 7, 3, 0, 1, 0],
    [5, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 8, 0, 6, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 2, 0],
    [0, 3, 6, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 9]
]

if solve_sudoku(sudoku_grid):
    print_grid(sudoku_grid)
else:
    print("No solution exists")
