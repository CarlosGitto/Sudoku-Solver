import numpy as np
from py_sudoku.functions.functions import *
from py_sudoku.get_sudoku import make_a_sudoku
import json


#============================MAIN===========================#


def func(sudoku, dict):
    # iniciamos el diccionario

    val_x_y_sqr(sudoku, dict)
    put_val(dict, sudoku)
    only_one_option_in_family(dict, sudoku)


def fun(old_sudoku, new_sudoku, wrk_pos):
    while True:
        if not np.array_equiv(old_sudoku, new_sudoku):
            old_sudoku = new_sudoku.copy()
            func(new_sudoku, wrk_pos)

        else:
            print("bien, se acabaron los valores faciles")
            break


def cicle_of_solving(sudoku, dict):
    for i in range(9):
        for j in range(9):
            if sudoku[i, j] == 0:
                ghst_values_chk(sudoku, dict, i, j)
            only_one_option_in_family(dict, sudoku)
    same_pos_and_val(dict)
    put_val(dict, sudoku)


def solve(my_sudoku):
    wrk_pos = dict()
    wrk_pos = dictionary(my_sudoku, wrk_pos)
    while 0 in my_sudoku:
        fun(sudoku_compare, my_sudoku, wrk_pos)
        cicle_of_solving(my_sudoku, wrk_pos)
    print(my_sudoku)


if __name__ == "__main__":
    my_sudoku = make_a_sudoku()
    solve(my_sudoku)
