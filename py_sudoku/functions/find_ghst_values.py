# ghs_values, son valores que estan en una familia ocupando misma fila o columna, haciendo que ese valor si o si vaya ahi
from py_sudoku.functions.find_ghst_x import ghst_values_x
from py_sudoku.functions.find_ghst_y import ghst_values_y
from py_sudoku.functions.return_family import func_abc

# encuentra posibles ghst_values y los manda a sus respectivas funciones(x o y)


def ghst_values_chk(sudoku, dict, i, j):

    ghst_lst_x = []
    ghst_name_x = []
    ghst_lst_y = []
    ghst_name_y = []
    family_items = []
    family = func_abc(dict, i, j)
    x = (family+str(i)+str(j))
    print("working with", x)
    for name, lst in dict.items():
        if name == x:
            continue

        elif family in name and type(lst) == list and type(dict[x]) == list and len(lst) > 1:
            family_items.append(name)

            if name[1] == str(i):
                print(name, "same row")
                for value in lst:
                    if value in dict[x] and value not in ghst_lst_x:
                        print(name, "agrego", value, "a ghst_x")
                        ghst_lst_x.append(value)
                        if name not in ghst_lst_x:
                            ghst_name_x.append(name)

            if name[2] == str(j):

                print(name, "same column")
                for value in lst:
                    if value in dict[x] and value not in ghst_lst_y:
                        print(name, "agrego", value, "a ghs_y")
                        ghst_lst_y.append(value)
                        if name not in ghst_lst_y:
                            ghst_name_y.append(name)

    print(ghst_name_x, ghst_name_y)
    print("family with list as values", family_items)
    values_to_remv = []

    for val in ghst_lst_x:
        if val in ghst_lst_y and val not in values_to_remv:
            values_to_remv.append(val)
        else:
            continue
    for values in values_to_remv:
        print(values, "se encuentra tanto en la fila como en la columna de",
              x, "no puede ser un ghst")
        ghst_lst_x.remove(values)
        ghst_lst_y.remove(values)

    if len(ghst_lst_x) == 0 and len(ghst_lst_y) == 0:
        print("no ghst found")
        return
    for nm in family_items:

        if nm in ghst_name_x or nm in ghst_name_y:
            continue
        else:
            for val in dict[nm]:
                print(nm, val)
                try:
                    if val in ghst_lst_x:
                        print("en", nm, val, "no es un ghst")
                        ghst_lst_x.remove(val)
                        print(val, "ah sido removido de la lista ghst")
                        print(ghst_lst_x)
                    if val in ghst_lst_y:
                        print("en", nm, val, "no es un ghst")
                        ghst_lst_y.remove(val)
                        print(val, "ah sido removido de la lista ghst")
                        print(ghst_lst_y)
                except:
                    continue

    if len(ghst_lst_x) != 0:
        print("final list of ghst_x for ", x, ghst_lst_x)
        ghst_values_x(sudoku[i], dict, i, j, ghst_lst_x, family)
    if len(ghst_lst_y) != 0:
        print("final list of ghst_y for ", x, ghst_lst_y)
        ghst_values_y(sudoku[:, j], dict, i, j, ghst_lst_y, family)
