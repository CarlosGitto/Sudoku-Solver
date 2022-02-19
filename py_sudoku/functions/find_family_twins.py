from py_sudoku.functions.remove_ghst import remove_ghst_values
from py_sudoku.functions.return_family import return_list_of_family
from better_functions.add_ghst import add_ghst
# Si hay igual cantidad de posiciones y valores, restringira los mismos para los demas elementos de la familia


def same_pos_and_val(ghst_dict: dict, dict: dict, key: str, my_sudoku: list):

    family = return_list_of_family(dict, key)
    list_of_keys = []
    print("working with ", key, dict[key])
    for member in family:
        if member != key and type(dict[member]) == list:
            print("we are comparing with ", member, dict[member])
            # miembros familiares con listas como valores
            list_of_keys.append(member)
            if len(dict[member]) == 0:
                print("found empty list", member, dict[member])
                raise ValueError

    twins_history = []

    for key_1 in list_of_keys:
        if key_1 in twins_history:
            continue
        family_twins = [key_1]
        find_ghs_x = [key_1]
        find_ghs_y = [key_1]
        for key_2 in list_of_keys:
            if dict[key_1] == dict[key_2] and key_1 != key_2 and key_2 not in family_twins:
                family_twins.append(key_2)
                if key_2[1] == key_1[1]:
                    find_ghs_x.append(key_2)
                if key_2[2] == key_1[2]:
                    if key_2 in find_ghs_x:
                        find_ghs_x.remove(key_2)
                    else:
                        find_ghs_y.append(key_2)
        if len(family_twins) > 1 and len(family_twins) == len(dict[key_1]):
            print("hay la misma cantidad de listas que de valores para",
                  dict[key_1], "y son: ", family_twins)
            for key_name in list_of_keys:
                if key_name in family_twins:
                    twins_history.append(key_name)
                    continue
                else:
                    for k in dict[key_1]:
                        try:
                            dict[key_name].remove(k)
                            add_ghst(ghst_dict, key_name, k)
                        except ValueError:
                            continue
                    print(dict[key_1], "fueron removidos de ",
                          key_name, "quedo", dict[key_name])

            if len(find_ghs_x) == len(family_twins):
                print("found ghsts", find_ghs_x, family_twins)
                remove_ghst_values(ghst_dict,
                                   dict[key_1], dict, key_1[1], find_ghs_x, True)
            if len(find_ghs_y) == len(family_twins):
                print("found ghsts", find_ghs_y, family_twins)
                remove_ghst_values(ghst_dict,
                                   dict[key_1], dict, key_1[2], find_ghs_y, False)
