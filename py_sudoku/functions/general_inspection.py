from better_functions.add_ghst import add_ghst
from better_functions.found_a_value import found_a_value
from better_functions.ghst_chek import can_be_added
from constantes import kn_lst
from py_sudoku.functions.return_family import return_family_key, return_list_of_family
# Encuentra un 0 en la matriz y devuelve valores que puede tomar por fila,columnay y familia


def fnd_kn_val(ghst_dict, sudoku_row, sudoku_clmn, dict, key):
    n = []
    for val in sudoku_row:
        if val != 0:
            n.append(val)
            #print("row", sudoku_row, val)

    for val in sudoku_clmn:
        if val != 0:
            n.append(val)

    family = return_list_of_family(dict, key)
    for member in family:
        if type(dict[member]) != list:
            #print(key, "append from ", member, dict[member])
            n.append(dict[member])

    final_values = set(n)
    pos_val = list(set(kn_lst)-final_values)
    return pos_val

 # Resuelve valores faciles


def val_x_y_sqr(ghst_dict: dict, sudoku: list, dict: dict):
    for key in dict.keys():
        i = int(key[1])
        j = int(key[2])

        if sudoku[i][j] == 0:
            if type(dict[key]) == list:

                pos_val = fnd_kn_val(
                    ghst_dict, sudoku[i], sudoku[:, j], dict, key)
                for value in pos_val:
                    if can_be_added(ghst_dict, value, key):
                        if value not in dict[key]:
                            dict[key].append(value)
                print("value added to", key, dict[key])
        else:
            if dict[key] == sudoku[i][j]:
                continue
            else:
                print("something is odd")
