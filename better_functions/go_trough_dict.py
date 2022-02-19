from better_functions.one_item_list import one_item_list
from py_sudoku.functions.find_family_horphan import horphan_in_family
from py_sudoku.functions.find_family_twins import same_pos_and_val
from py_sudoku.functions.general_inspection import fnd_kn_val
from better_functions.ghst_chek import can_be_added
import numpy as np


def go_trough_dict(ghst_dict: dict, my_dict: dict, my_sudoku: list, round: int, solution: list) -> None:
    print(my_sudoku)
    print("solution \n", solution)
    for key in my_dict.keys():
        print("dict", my_dict)
        i = int(key[1])
        j = int(key[2])
        if round == 0:
            if type(my_dict[key]) == list:
                print("this ", key, my_dict[key])
                easy_values = fnd_kn_val(ghst_dict, my_sudoku[i],
                                         my_sudoku[:, j], my_dict, key)
                my_dict[key] = easy_values
                continue
            else:
                continue
        if type(my_dict[key]) == list:
            horphan_in_family(
                ghst_dict, my_dict, my_sudoku, key)
            print("inside", key, my_dict[key])
            if len(my_dict[key]) == 1:
                one_item_list(ghst_dict, key, my_dict, my_sudoku)
            if type(my_dict[key]) == list and len(my_dict[key]) > 1:
                print('we are in easy values')
                easy_values = fnd_kn_val(ghst_dict, my_sudoku[i],
                                         my_sudoku[:, j], my_dict, key)
                print(easy_values, key)
                if len(easy_values) == 1:
                    my_dict[key] = easy_values
                    one_item_list(ghst_dict, key, my_dict, my_sudoku)
                    continue
                else:
                    if my_dict[key] != easy_values:
                        for item in easy_values:
                            if item in my_dict[key]:
                                continue
                            if can_be_added(ghst_dict, item, key):
                                my_dict[key].append(item)
                        else:
                            continue
                    same_pos_and_val(ghst_dict, my_dict, key, my_sudoku)
            if type(my_dict[key]) == list and len(my_dict[key]) == 0:
                print("something went wrong in", key, my_dict[key])
                print("dict", my_dict, "\n")
                print("ghst", ghst_dict)
                raise ValueError
        else:
            if my_sudoku[i][j] == my_dict[key]:
                pass
            elif type(my_dict[key]) == int or type(my_dict[key]) == np.int64:
                my_sudoku[i][j] = my_dict[key]
            else:
                print("something broke")
                raise ValueError
