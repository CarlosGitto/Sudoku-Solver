from better_functions.found_a_value import found_a_value
from better_functions.add_ghst import add_ghst
from better_functions.remove_old_ghst import remove_old_ghst


def one_item_list(ghst_dict: dict, key: str, my_dict: dict, sudoku: list):
    print("value found", key, my_dict[key])
    my_dict[key] = my_dict[key][0]
    print("value updated", key, my_dict[key])
    i = int(key[1])
    j = int(key[2])
    sudoku[i][j] = my_dict[key]
    print(sudoku)
    remove_old_ghst(ghst_dict, my_dict, key)
    found_a_value(ghst_dict, key, my_dict, sudoku)
