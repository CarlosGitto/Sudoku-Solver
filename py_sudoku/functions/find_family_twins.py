from py_sudoku.constantes import kn_lst_3
# Si hay igual cantidad de posiciones y valores, restringira los mismos para los demas elementos de la familia


def same_pos_and_val(dict):
    for ch in kn_lst_3:
        list_of_keys = []
        for key in dict.keys():
            if key[0] == ch and type(dict[key]) == list:
                list_of_keys.append(key)
                print(key, dict[key])

        twins_history = []

        for key_1 in list_of_keys:
            if key_1 in twins_history:
                continue
            family_twins = [key_1]
            for key_2 in list_of_keys:
                if dict[key_1] == dict[key_2] and key_1 != key_2 and key_2 not in family_twins:
                    family_twins.append(key_2)
            if len(family_twins) > 1:
                print("listas iguales", family_twins)
                if len(family_twins) == len(dict[key_1]):
                    print("hay la misma cantidad de listas que de valores para",
                          dict[key_1], "y son: ", family_twins)
                    for k in list_of_keys:
                        if k not in family_twins:
                            dict[k] = [k for k in (
                                set(dict[k]) - set(dict[key_1]))]
                            print(dict[key_1], "fueron removidos de ",
                                  k, "quedo", dict[k])
                        if k in family_twins:
                            twins_history.append(k)
