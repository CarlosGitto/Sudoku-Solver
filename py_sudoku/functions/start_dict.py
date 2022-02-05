"""This file is in charge of create the dict of the sudoku"""
from py_sudoku.constantes import kn_lst_3 as kn_lst


def big_dict(sudoku):
    n = 0
    k = 0
    my_dict = {}
    for index, key in enumerate(kn_lst):

        if index >= 3:
            n = 3
            if index >= 6:
                n = 6
        if index % 3 == 0:
            const = 0
        k *= const
        for i in range(n, n+3):
            for j in range(k, k+3):
                if sudoku[i][j] != 0:
                    my_dict[f"{key}{i}{j}"] = sudoku[i][j]
                else:
                    my_dict[f"{key}{i}{j}"] = 0
        k = 3
        const += 1
    return my_dict
