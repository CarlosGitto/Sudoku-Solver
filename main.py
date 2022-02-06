import numpy as np
import time
from py_sudoku.functions.remove_single_int_list import remove_single_int_list
from py_sudoku.functions.find_family_horphan import only_one_option_in_family
from py_sudoku.functions.find_family_twins import same_pos_and_val
from py_sudoku.functions.find_ghst_values import ghst_values_chk
from py_sudoku.functions.start_dict import big_dict
from py_sudoku.functions.general_inspection import val_x_y_sqr
from py_sudoku.get_sudoku import make_a_sudoku
from py_sudoku.constantes import sudoku_compare

#============================MAIN===========================#


def func(sudoku, dict):
    # iniciamos el diccionario

    val_x_y_sqr(sudoku, dict)
    remove_single_int_list(dict, sudoku)
    only_one_option_in_family(dict, sudoku)


def fun(old_sudoku, new_sudoku, wrk_pos):
    while True:
        if not np.array_equiv(old_sudoku, new_sudoku):
            old_sudoku = new_sudoku.copy()
            func(new_sudoku, wrk_pos)

        else:
            print("bien, se acabaron los valores faciles")
            #x = {}
            """ for key, val in wrk_pos.items():
                if type(val) == list:
                    x[key] = val
            print(x) """

            # print(new_sudoku)
            break


def cicle_of_solving(sudoku, dict):
    for i in range(9):
        for j in range(9):
            if sudoku[i, j] == 0:
                ghst_values_chk(sudoku, dict, i, j)
            only_one_option_in_family(dict, sudoku)
    same_pos_and_val(dict)
    remove_single_int_list(dict, sudoku)


def solve(my_sudoku):
    wrk_pos = dict()
    wrk_pos = big_dict(my_sudoku)
    while 0 in my_sudoku:
        fun(sudoku_compare, my_sudoku, wrk_pos)
        cicle_of_solving(my_sudoku, wrk_pos)

    print(my_sudoku)


if __name__ == "__main__":
    start = time.time()
    my_sudoku, difficulty = make_a_sudoku()
    solve(my_sudoku)
    print("difficulty: ", difficulty)
    end = time.time()
    print("time ", end - start)
