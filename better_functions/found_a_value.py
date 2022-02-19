from better_functions.add_ghst import add_ghst


def found_a_value(ghst_dict: dict, solved_key: str, my_dict: dict, sudoku: list):
    updated_keys = []
    for key in my_dict.keys():
        if type(my_dict[key]) == list and my_dict[solved_key] in my_dict[key]:
            if key[0] == solved_key[0]:
                my_dict[key].remove(my_dict[solved_key])
                add_ghst(my_dict, key, my_dict[solved_key])
                updated_keys.append(key)
                print(key, my_dict[key], "value to remove",
                      solved_key, my_dict[solved_key])
            else:
                if key[1] == solved_key[1] or key[2] == solved_key[2]:
                    my_dict[key].remove(my_dict[solved_key])
                    updated_keys.append(key)
                    add_ghst(ghst_dict, key, my_dict[solved_key])
                    print(key, my_dict[key], "value to remove",
                          solved_key, my_dict[solved_key])
