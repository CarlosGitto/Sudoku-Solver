import json
from get_sudoku import check_difficult
import numpy as np


def same_sudoku():
    file = open("sudoku.json", "r")

    x = json.loads(file.read())
    difficulty = check_difficult(x['nivel'])
    initial_sudoku = x["sudoku"].replace(".", "0")
    print(initial_sudoku)
    sudokus = [initial_sudoku, x["solucion"]]
    my_sudokus = []
    for i, sudoku in enumerate(sudokus):
        final_sudoku = []
        x = len(sudoku)
        n = 9
        for index in range(0, x, n):
            final_sudoku.append(list(sudoku[index: index + n]))

        for i, sub_list in enumerate(final_sudoku):
            final_sudoku[i] = [int(k) for k in sub_list]

        my_sudokus.append(np.array(final_sudoku))

    return my_sudokus[0], my_sudokus[1], difficulty
