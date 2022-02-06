# ghs_values, son valores que estan en una familia ocupando misma fila o columna, haciendo que ese valor si o si vaya ahi
from py_sudoku.functions.remove_ghst import remove_ghst_values
from py_sudoku.functions.return_family import func_abc

# encuentra posibles ghst_values y los manda a sus respectivas funciones(x o y)


def ghst_values_chk(sudoku, dict, i, j):
    ghst_lst_x = []
    ghst_name_x = []
    ghst_lst_y = []
    ghst_name_y = []
    family_items = []
    family = func_abc(dict, i, j)
    key_selected = (family+str(i)+str(j))
    print("working with", key_selected)
    if type(dict[key_selected]) == list:
        for key in dict.keys():

            if key == key_selected:
                continue
            if family == key[0] and type(dict[key]) == list and len(dict[key]) > 1:
                family_items.append(key)

                if key[1] == str(i):

                    print(key, "same row")
                    for value in dict[key]:
                        if value in dict[key_selected] and value not in ghst_lst_x:
                            print(key, dict[key], "agrego", value, "a ghst_x")
                            ghst_lst_x.append(value)
                            if key not in ghst_name_x:
                                print("hola")
                                ghst_name_x.append(key)

                if key[2] == str(j):

                    print(key, "same column")
                    for value in dict[key]:
                        if value in dict[key_selected] and value not in ghst_lst_y:
                            print(key, "agrego", value, "a ghs_y")
                            ghst_lst_y.append(value)
                            if key not in ghst_name_y:
                                print("chau")
                                ghst_name_y.append(key)

        print(ghst_name_x, ghst_name_y)
        print("family with list of values", family_items)
        values_to_remv = []

        for val in ghst_lst_x:
            if val in ghst_lst_y and val not in values_to_remv:
                values_to_remv.append(val)
            else:
                continue
        for values in values_to_remv:
            print(values, "se encuentra tanto en la fila como en la columna de",
                  key_selected, "no puede ser un ghst")
            ghst_lst_x.remove(values)
            ghst_lst_y.remove(values)

        for nm in family_items:
            if len(ghst_lst_x) == 0 and len(ghst_lst_y) == 0:
                print("no ghst found")
                return

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
                            if len(ghst_lst_x) == 0:
                                return
                        if val in ghst_lst_y:
                            print("en", nm, val, "no es un ghst")
                            ghst_lst_y.remove(val)
                            print(val, "ah sido removido de la lista ghst")
                            print(ghst_lst_y)
                            if len(ghst_lst_y) == 0:
                                return
                    except:
                        continue

        if len(ghst_lst_x) != 0:
            print("final list of ghst_x for ", key_selected, ghst_lst_x)
            remove_ghst_values(sudoku[i], dict, i,
                               ghst_lst_x, family, row_type=True)
        if len(ghst_lst_y) != 0:
            print("final list of ghst_y for ", key_selected, ghst_lst_y)
            remove_ghst_values(sudoku[:][j], dict, j,
                               ghst_lst_y, family, row_type=False)

    # input()
