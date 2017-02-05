"""
SudokuPyCSF - Solve sudoku with Python using CSF approach
Version : 1.0.0
Author : Hamidreza Mahdavipanah
Repository: http://github.com/mahdavipanah/SudokuPyCSF
License : MIT License
"""
import math

from mrv_backtracking import mrv_domains
from backtracking import backtracking_search


def var_selector(sudoku):
    min_domains = mrv_domains(sudoku)

    if not min_domains:
        return None, None, None

    if len(min_domains) == 1:
        var = min_domains.popitem()
        return var[0][0], var[0][1], var[1]

    ret_degree = None
    ret_i, ret_j = None, None

    sqrt_n = int(math.sqrt(len(sudoku)))
    qs = range(sqrt_n)

    for i, j in min_domains.keys():
        degree = 0

        # Check row
        for var in sudoku[i]:
            if var == 0:
                degree += 1

        # Check column
        for row in sudoku:
            if row[j] == 0:
                degree += 1

        # Check block
        block_i = int(i / sqrt_n)
        block_j = int(j / sqrt_n)
        for column in [block_i * sqrt_n + q for q in qs]:
            for row in [block_j * sqrt_n + q for q in qs]:
                if sudoku[column][row] == 0:
                    degree += 1

        if ret_degree is not None:
            if degree > ret_degree:
                ret_degree = degree
                ret_i, j = i, j
        else:
            ret_degree = degree
            ret_i, ret_j = i, j

        return i, j, min_domains[i, j]


def search(sudoku):
    return backtracking_search(sudoku, var_selector, True)
