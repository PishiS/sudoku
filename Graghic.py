import matplotlib.pyplot as plt
import numpy as np

def draw_sudoku(grid):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 9)
    
    # Draw the grid
    for i in range(10):
        if i % 3 == 0:
            ax.plot([i, i], [0, 9], 'k', linewidth=2)
            ax.plot([0, 9], [i, i], 'k', linewidth=2)
        else:
            ax.plot([i, i], [0, 9], 'k', linewidth=1)
            ax.plot([0, 9], [i, i], 'k', linewidth=1)
    
    # Fill in the numbers
    for row in range(9):
        for col in range(9):
            num = grid[row][col]
            if num != 0:
                ax.text(col + 0.5, 8.5 - row, str(num), fontsize=16, ha='center', va='center')

    ax.set_xticks([])
    ax.set_yticks([])
    plt.gca().invert_yaxis()
    plt.show()

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

draw_sudoku(sudoku_grid)
