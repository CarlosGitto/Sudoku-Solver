from py_sudoku.functions.return_family import func_abc
# Devuelve una lista con los posibles valores de toda una familia(solo de los familiares==0)


def func_sqr(dict, i, j):
    k = []
    name_sqr = func_abc(dict, i, j)
    for name, val in dict.items():
        if name.startswith(name_sqr):
            if type(val) != list and val != 0:
                k.append(val)
            else:
                continue
    return(k)
