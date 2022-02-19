import numpy as np
import time


from better_functions.go_trough_dict import go_trough_dict
from better_functions.start_dict import big_dict
from py_sudoku.functions.general_inspection import val_x_y_sqr
from get_sudoku import make_a_sudoku
from use_same_sudoku import same_sudoku

#============================MAIN===========================#


def func(ghst_pos: dict, sudoku: list, dict: dict):
    # iniciamos el diccionario

    val_x_y_sqr(ghst_pos, sudoku, dict)
    print("hola")


def fun(ghst_pos, old_sudoku, new_sudoku, wrk_pos):
    while True:
        if not np.array_equiv(old_sudoku, new_sudoku):
            old_sudoku = new_sudoku.copy()
            return True

        else:
            print("bien, se acabaron los valores faciles")
            return False


def is_solved(sudoku, wrk_pos, ghst_pos):
    if 0 in sudoku:
        print("dict", wrk_pos)
        print("ghst", ghst_pos)
        print(my_sudoku)
        return False
    else:
        print("dict", wrk_pos)
        print("ghst", ghst_pos)
        print(my_sudoku)
        return True


def solve(my_sudoku, solution):
    wrk_pos = dict()
    wrk_pos, ghst_pos = big_dict(my_sudoku)
    state = is_solved(my_sudoku, wrk_pos, ghst_pos)
    round = 0
    while not state:  # state = false -> there are 0 un sudoku
        print('solution \n', solution)
        go_trough_dict(ghst_pos, wrk_pos, my_sudoku, round, solution)
        #remove_old_ghst(ghst_pos, wrk_pos)
        round += 1
        state = is_solved(my_sudoku, wrk_pos, ghst_pos)
        print("dict", wrk_pos)
        print("ghst", ghst_pos)
        print(my_sudoku)
        print("solution \n", solution)


if __name__ == "__main__":
    start = time.time()
    my_sudoku, solution, difficulty = make_a_sudoku()
    solve(my_sudoku, solution)
    print("difficulty: ", difficulty)
    if np.array_equiv(my_sudoku, solution):
        print("good solution")
    else:
        print("bad solution")
    end = time.time()
    print("time ", end - start)
