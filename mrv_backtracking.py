"""
SudokuPyCSF - Solve sudoku with Python using CSF approach
Version : 1.0.0
Author : Hamidreza Mahdavipanah
Repository: http://github.com/mahdavipanah/SudokuPyCSF
License : MIT License
"""
import math

from backtracking import backtracking_search


def mrv_domains(sudoku):
    domains_dict = {}
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j] == 0:
                domains_dict[i, j] = set(range(1, len(sudoku) + 1))

    sqrt_n = int(math.sqrt(len(sudoku)))

    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if type(sudoku[i][j]) is not set:
                qs = range(sqrt_n)
                block_i = int(i / sqrt_n)
                block_i_set = {block_i * sqrt_n + q for q in qs}
                block_j = int(j / sqrt_n)
                block_j_set = {block_j * sqrt_n + q for q in qs}

                for k in domains_dict.keys():
                    # Are in same row
                    # or
                    # in same column
                    # or
                    # in same block
                    if k[0] == i or k[1] == j or (k[0] in block_i_set and k[1] in block_j_set):
                        domains_dict[k].discard(sudoku[i][j])

    min_remaining_val = None;
    for domain in domains_dict.values():
        if min_remaining_val is not None:
            min_remaining_val = min(min_remaining_val, len(domain))
        else:
            min_remaining_val = len(domain)

    # Sudoku can't be solved
    if min_remaining_val == 0:
        return None

    min_domains = {k: domains_dict[k]
                   for k in domains_dict.keys()
                   if len(domains_dict[k]) == min_remaining_val}

    return min_domains


def var_selector(sudoku):
    min_domains = mrv_domains(sudoku)

    if not min_domains:
        return None, None, None

    var = min_domains.popitem()
    return var[0][0], var[0][1], var[1]


def search(sudoku):
    return backtracking_search(sudoku, var_selector, True)
