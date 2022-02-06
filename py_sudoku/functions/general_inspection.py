from py_sudoku.constantes import kn_lst
from py_sudoku.functions.return_family_options import func_sqr
# Encuentra un 0 en la matriz y devuelve valores que puede tomar por fila,columnay y familia


def fnd_kn_val(sudoku_row, sudoku_clmn, dict, i, j):
    n = []

    for val in sudoku_row:
        if val != 0:
            n.append(val)

    for val in sudoku_clmn:
        if val != 0:
            n.append(val)

    sub_sqr = func_sqr(dict, i, j)
    for val in sub_sqr:
        if val != 0:
            n.append(val)

    final_values = set(n)
    pos_val = list(set(kn_lst)-final_values)
    return(pos_val)

 # Resuelve valores faciles


def val_x_y_sqr(sudoku, dict):
    for key in dict.keys():
        i = int(key[1])
        j = int(key[2])
        if sudoku[i][j] == 0:
            pos_val = fnd_kn_val(sudoku[i], sudoku[:, j], dict, i, j)
            dict[key] = pos_val

            print("valores actualizado para", key)
