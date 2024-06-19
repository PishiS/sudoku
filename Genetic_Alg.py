import numpy as np
import random
from copy import deepcopy

# Example Sudoku grid with 0 representing empty cells
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

def fitness(grid):
    score = 0
    for row in grid:
        score += len(set(row))
    for col in zip(*grid):
        score += len(set(col))
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = []
            for r in range(3):
                for c in range(3):
                    box.append(grid[box_row + r][box_col + c])
            score += len(set(box))
    return score

def create_population(size, grid):
    population = []
    for _ in range(size):
        individual = deepcopy(grid)
        for row in range(9):
            available_numbers = set(range(1, 10)) - set(individual[row])
            for col in range(9):
                if individual[row][col] == 0:
                    individual[row][col] = random.choice(list(available_numbers))
                    available_numbers.remove(individual[row][col])
        population.append(individual)
    return population

def select(population):
    population = sorted(population, key=lambda x: fitness(x), reverse=True)
    return population[:len(population)//2]

def crossover(parent1, parent2):
    point = random.randint(0, 8)
    child = deepcopy(parent1)
    for i in range(point, 9):
        child[i] = parent2[i]
    return child

def mutate(individual, mutation_rate=0.1):
    for row in range(9):
        if random.random() < mutation_rate:
            col1, col2 = random.sample(range(9), 2)
            individual[row][col1], individual[row][col2] = individual[row][col2], individual[row][col1]
    return individual

def genetic_algorithm(grid, population_size=1000, generations=1000):
    population = create_population(population_size, grid)
    for generation in range(generations):
        population = select(population)
        next_generation = []
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(population, 2)
            child = crossover(parent1, parent2)
            child = mutate(child)
            next_generation.append(child)
        population = next_generation
        best_individual = max(population, key=lambda x: fitness(x))
        if fitness(best_individual) == 243:
            return best_individual
    return None

solution = genetic_algorithm(sudoku_grid)

if solution:
    for row in solution:
        print(row)
else:
    print("No solution found")

