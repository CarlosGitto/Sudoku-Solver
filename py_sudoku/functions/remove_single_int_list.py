

def remove_single_int_list(my_dict, sudoku):

    for key, value in my_dict.items():
        if type(value) == list and len(value) == 1 and value != 0:
            my_dict[key] = my_dict[key][0]
            # actualiza un valor que posee una unica posibilidad en el diccionario
            # tambien actualiza el sudoku
            i = int(key[1])
            j = int(key[2])
            ch = key[0]
            sudoku[i][j] = my_dict[key]
            print(key, ":", my_dict[key])
            for sub_key in my_dict.keys():

                if ch in sub_key and type(my_dict[sub_key]) == list:

                    try:
                        my_dict[sub_key].remove(my_dict[key])
                        print(key, "is ",
                              my_dict[key], "so it has been removed from ", sub_key, my_dict[sub_key])

                    except ValueError:
                        continue
    # input()
