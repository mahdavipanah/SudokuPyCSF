"""
SudokuPyCSF - Solve sudoku with Python using CSF approach
Version : 1.0.0
Author : Hamidreza Mahdavipanah
Repository: http://github.com/mahdavipanah/SudokuPyCSF
License : MIT License
"""
from backtracking import backtracking_search


def var_selector(sudoku):
    for i in range(len(sudoku)):
        for j in range(len(sudoku)):
            if sudoku[i][j] == 0:
                return i, j, range(1, len(sudoku) + 1)


def search(sudoku):
    return backtracking_search(sudoku, var_selector)
