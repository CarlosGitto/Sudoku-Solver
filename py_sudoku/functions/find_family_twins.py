from py_sudoku.constantes import kn_lst_3
# Si hay igual cantidad de posiciones y valores, restringira los mismos para los demas elementos de la familia


def same_pos_and_val(dict):
    for ch in kn_lst_3:
        name_random = []
        for name, val in dict.items():
            if name.startswith(ch) and type(val) == list:
                name_random.append(name)
                print(name, val)

        for n in name_random:
            list_random = [n]
            for i in range(len(name_random)):
                if dict[n] == dict[name_random[i]] and i > name_random.index(n) and i not in list_random:
                    list_random.append(name_random[i])
            if len(list_random) > 1:
                print("listas iguales", list_random)
            if len(list_random) == len(dict[n]):
                print("hay la misma cantidad de listas que de valores para",
                      list_random, dict[n], n)
                for names in name_random:
                    if names not in list_random:
                        for val in dict[n]:
                            if val in dict[names]:
                                dict[names].remove(val)
                                print(val, "fue removido de ",
                                      names, dict[names])
