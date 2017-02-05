"""
SudokuPyCSF - Solve sudoku with Python using CSF approach
Version : 1.0.0
Author : Hamidreza Mahdavipanah
Repository: http://github.com/mahdavipanah/SudokuPyCSF
License : MIT License
"""
import math
from random import randint


def var_conflicts(sudoku, var_i, var_j, new_val=None):
    if new_val:
        val = new_val
    else:
        val = sudoku[var_i][var_j]

    var_conflicts = 0

    # Check row
    for j in range(len(sudoku)):
        if sudoku[var_i][j] != 0 and sudoku[var_i][j] == val and j != var_j:
            var_conflicts += 1

    # Check column
    for i in range(len(sudoku)):
        if sudoku[i][var_j] != 0 and sudoku[i][var_j] == val and i != var_i:
            var_conflicts += 1

    # Check block
    sqrt_n = int(math.sqrt(len(sudoku)))
    block_i = int(var_i / sqrt_n)
    block_j = int(var_j / sqrt_n)
    qs = range(sqrt_n)
    for i in [block_i * sqrt_n + q for q in qs]:
        for j in [block_j * sqrt_n + q for q in qs]:
            if (i, j) != (var_i, var_j) and sudoku[i][j] != 0 and sudoku[i][j] == val:
                var_conflicts += 1

    return var_conflicts


def sudoku_conflicts(sudoku):
    sum_conflicts = 0
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            sum_conflicts += var_conflicts(sudoku, i, j)

    return sum_conflicts


def search(sudoku, max_steps):
    # Find fixed vars and randomize the sudoku
    fixed_vars = set()
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j] != 0:
                fixed_vars.add((i, j))
            else:
                sudoku[i][j] = randint(1, len(sudoku))

    domain = set(range(1, len(sudoku) + 1))

    i = 0
    while i < max_steps:
        sum_conflicts = sudoku_conflicts(sudoku)
        if sum_conflicts == 0:
            return sudoku, 0

        rand_i = randint(0, 8)
        rand_j = randint(0, 8)
        if (rand_i, rand_j) in fixed_vars:
            continue

        for val in domain:
            if var_conflicts(sudoku, rand_i, rand_j) > var_conflicts(sudoku, rand_i, rand_j, val):
                sudoku[rand_i][rand_j] = val

        i += 1

    return sudoku, sum_conflicts
