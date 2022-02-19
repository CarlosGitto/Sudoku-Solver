from better_functions.add_ghst import add_ghst
# Adueña de una fila a un valor


def remove_ghst_values(ghst_dict: dict, twins: list, dict: dict, pointer: int, ghst_name_lst: list, row_type: bool):

    for key in dict.keys():
        if type(dict[key]) == list:
            if row_type:
                if pointer in key[1] and key not in ghst_name_lst:
                    print(twins, "removed from", key, dict[key])
                    dict[key] = [k for k in dict[key] if k not in twins]
                    for values in twins:
                        add_ghst(ghst_dict, key, values)
                    print("prueba", dict[key])
            else:
                if pointer in key[2] and key not in ghst_name_lst:
                    print(twins, "removed from", key, dict[key])
                    dict[key] = [k for k in dict[key] if k not in twins]
                    for values in twins:
                        add_ghst(ghst_dict, key, values)
                    print("prueba", dict[key])
