#!/usr/bin/env python3
"""
SudokuPyCSF - Solve sudoku with Python using CSF approach
Version : 1.0.0
Author : Hamidreza Mahdavipanah
Repository: http://github.com/mahdavipanah/SudokuPyCSF
License : MIT License
"""
import os
import platform
import sys

import simple_backtracking
import mrv_backtracking
import mrv_degree_backtracking
import min_conflict

from input import sudoku

platform_system = platform.system()


def clear_screen():
    if platform_system == 'Linux':
        os.system('clear')
    elif platform_system == 'Windows':
        os.system('cls')


while True:
    clear_screen()
    print("Algorithms :")
    print("    1- Simple backtracking")
    print("    2- Backtracking with MRV heuristic")
    print("    3- Backtracking with MRV and degree heuristic")
    print("    4- Minimum conflicts local search\n")
    print("    0- Exit")
    try:
        option = int(input("Enter a number: "))
        if option < 0 or option > 4:
            raise Exception
    except:
        continue

    break

if option == 0:
    sys.exit(0)

result = None

if option == 1:
    result = simple_backtracking.search(sudoku)
elif option == 2:
    result = mrv_backtracking.search(sudoku)
elif option == 3:
    result = mrv_degree_backtracking.search(sudoku)
elif option == 4:
    max_steps = -1
    while True:
        try:
            max_steps = int(input("Number of steps: "))
        except:
            print("Enter a integer number > 0 or 0 to Exit")
            continue
        break

    if max_steps == 0:
        sys.exit(0)

    result, sum_conflicts = min_conflict.search(sudoku, max_steps)

if result is None:
    print("This sudoku is not solvable!")
else:
    str_lines = []
    print("Result:")
    for row in result:
        str_lines.append(str(row))
    if option == 4:
        str_lines.append("Conflicts: {}".format(sum_conflicts))

    str = '\n'.join(str_lines)
    print(str)

    try:
        with open('output.txt', 'w') as file:
            file.write(str)
    except:
        pass
