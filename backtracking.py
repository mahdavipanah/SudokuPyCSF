"""
SudokuPyCSF - Solve sudoku with Python using CSF approach
Version : 1.0.0
Author : Hamidreza Mahdavipanah
Repository: http://github.com/mahdavipanah/SudokuPyCSF
License : MIT License
"""
import math


def sudoku_is_complete(sudoku):
    for row in sudoku:
        for var in row:
            if var == 0:
                return False
    return True


def value_is_consistent(sudoku, var_i, var_j, val):
    # Check row
    for var in sudoku[var_i]:
        if var != 0 and var == val:
            return False

    # Check column
    for row in sudoku:
        if row[var_j] != 0 and row[var_j] == val:
            return False

    # Check block
    sqrt_n = int(math.sqrt(len(sudoku)))
    block_i = int(var_i / sqrt_n)
    block_j = int(var_j / sqrt_n)
    qs = range(sqrt_n)
    for i in [block_i * sqrt_n + q for q in qs]:
        for j in [block_j * sqrt_n + q for q in qs]:
            if (i, j) != (var_i, var_j) and sudoku[i][j] != 0 and sudoku[i][j] == val:
                return False

    return True


def backtracking_search(sudoku, var_selector, check=None):
    if sudoku_is_complete(sudoku):
        return sudoku

    var_i, var_j, domain = var_selector(sudoku)

    for val in domain:
        if check:
            if type(check) is bool:
                if not check:
                    continue
            else:
                if not check(sudoku, var_i, var_j, val):
                    continue
        else:
            if not value_is_consistent(sudoku, var_i, var_j, val):
                continue

        sudoku[var_i][var_j] = val
        result = backtracking_search(sudoku, var_selector)
        if result:
            return result
        sudoku[var_i][var_j] = 0
