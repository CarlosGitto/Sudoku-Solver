from better_functions.compare_two_list import compare_list
from py_sudoku.functions.return_family import return_list_of_family
# Encuentra valores no repetidos para una lista que viene  de la familia

# busca posibles valores que solo un elemento puede tomar en la familia


def compare(lst: list) -> list:
    horphan = []
    horphan_history = []
    for sub_lst in lst:
        for value in sub_lst:
            if value not in horphan_history:
                horphan.append(value)
                horphan_history.append(value)
            else:
                try:
                    horphan.remove(value)
                except ValueError:
                    continue

    print("the horphans in ", lst, "are", horphan)

    return horphan


def only_one_option_in_family(ghst_dict, dict, sudoku, key):
    family = return_list_of_family(dict, key)
    family_values = []
    for member in family:
        if type(dict[member]) == list:
            family_values.append(dict[key])
        else:
            family.remove(member)
    print("working with ", key, dict[key])
    print("lista de familia", family)
    print("respective values", family_values)
    horphans = compare(family_values)
    for horphan in horphans:
        for name in family:
            try:
                if horphan in dict[name]:
                    dict[name] = [horphan]
            except TypeError:
                continue


def horphan_in_family(ghst_dict, dict, sudoku, key):
    family = return_list_of_family(dict, key)
    posible_horphans = [x for x in dict[key]]
    print("before loop", key, dict[key], 'family', family)
    family.remove(key)
    for member in family:
        if type(dict[member]) == list:
            for value in dict[key]:
                if value in dict[member]:
                    try:
                        posible_horphans.remove(value)
                    except ValueError:
                        continue  # the value has already been deleted
        else:
            try:
                dict[key].remove(dict[member])
                posible_horphans.remove(dict[member])
            except ValueError:
                continue  # remove a value that has been found

    print("after loop", key, dict[key], 'horphans', posible_horphans)

    if len(posible_horphans) == 1:
        print("found an horphan", posible_horphans)
        print("is from", key, dict[key])
        dict[key] = [x for x in posible_horphans]
    else:
        print("no horphans for", key, dict[key])
