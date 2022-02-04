from py_sudoku.constantes import *


#================================================================#
#                  Inicializa el diccionario                     #
#================================================================#
def dictionary(sudoku, wrk_pos):
    i = -1
    j = -1
    if len(wrk_pos) < 81:
        for row in kn_lst_2:
            for h in range(3):
                i += 1  # crea el dict con el estado inicial
                for ch in row:
                    for k in range(3):
                        j += 1
                        if j == 9:
                            j = 0
                        wrk_pos.update({"{}{}".format((ch), str(i)+str(j)): 0})

                        if sudoku[i, j] != 0:
                            wrk_pos.update(
                                {"{}{}".format((ch), str(i)+str(j)): (int(sudoku[i][j]))})
    return wrk_pos
#===================================================================================#
#                           Dividen Sudoku                                          #
#                                                                                   #
#===================================================================================#


# Devuelve el nombre de familia a partir de pos i,j
def func_abc(dict, i, j):
    x = str(i)+str(j)
    for name, val in dict.items():
        if x in name:
            return(name[0])

# Devuelve el nombre de familia a partir del nombre completo


def func_abc2(dict, nm, value):
    for name, val in dict.items():
        if nm[0] in name:
            return(name[0])

###########################################################################
#               Encargado de poner valores unicos                         #
###########################################################################


def put_val(dict, sudoku):
    for name, val in dict.items():
        i = int(name[1])
        j = int(name[2])
        ch = name[0]
        # actualiza un valor que posee una unica posibilidad en el diccionario
        if type(val) == list and len(val) == 1:
            # tambien actualiza el sudoku
            x = val[0]
            dict[name] = x
            sudoku[i, j] = x
            print(name, ":", x)

            for nm, value in dict.items():
                # quita el valor actualizado de la familia
                if ch in nm and type(value) == list and x in value:
                    value.remove(x)
                    print(nm, value)
                else:
                    continue
#===================================================================================#
#                           Encuentran Valores                                      #
#                                                                                   #
#===================================================================================#
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


# Encuentra valores no repetidos para una lista que viene  de la familia
def count_last_chk(lst):
    for i in lst:
        count = 0
        for j in range(len(lst)):
            if i == lst[j]:
                count += 1
        if count == 1:
            return(i)


# Encuentra un 0 en la matriz y devuelve valores que puede tomar por fila,columnay y familia
def fnd_kn_val(sudoku_row, sudoku_clmn, dict, i, j):
    n = []

    for val in sudoku_row:
        if val != 0:
            n.append(val)

    for val in sudoku_clmn:
        if val != 0:
            n.append(val)

    sub_sqr = func_sqr(dict, i, j)
    for val in sub_sqr:
        if val != 0:
            n.append(val)

    final_values = set(n)
    pos_val = list(set(kn_lst)-final_values)
    return(pos_val)

 # Resuelve valores faciles


def val_x_y_sqr(sudoku, dict):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                pos_val = fnd_kn_val(sudoku[i], sudoku[:, j], dict, i, j)
                for name, val in dict.items():
                    if (str(i)+str(j)) in name and dict[name] != pos_val:
                        dict.update({name: pos_val})
                        print("valores actualizado para", name)
# busca posibles valores que solo un elemento puede tomar en la familia


def only_one_option_in_family(dict, sudoku):
    for ch in kn_lst_3:
        summ = []
        for name, val in dict.items():
            if ch in name and type(val) == list:
                summ += dict[name]
        x = count_last_chk(summ)
        for name, val in dict.items():
            if ch in name and type(val) == list and x in val:
                dict.update({name: x})
                sudoku[int(name[1]), int(name[2])] = x
                print(name, ":", x)


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


# Adueña de una fila a un valor
def ghst_values_x(sudoku_row, dict, i, j, lst_ghst, family):
    sum = -1

    for value in sudoku_row:
        sum += 1
        numbers = str(i)+str(sum)
        for name in dict.keys():
            if numbers in name and value == 0 and type(dict[name]) == list and family not in name:
                for ghst in lst_ghst:
                    if ghst in dict[name]:
                        print(name, dict[name])
                        print(ghst, "es un ghst y fue removido de", name)
                        (dict[name]).remove(ghst)
                        print(name, dict[name])


# Adueña de una columna a un valor
def ghst_values_y(sudoku_colmn, dict, i, j, lst_ghst, family):
    sum = -1
    for value in sudoku_colmn:
        sum += 1
        numbers = str(sum)+str(j)
        for name in dict.keys():
            if numbers in name and value == 0 and type(dict[name]) == list and family not in name:
                for ghst in lst_ghst:
                    if ghst in dict[name]:
                        print(name, dict[name])
                        print(ghst, "es un ghst y fue removido de", name)

                        (dict[name]).remove(ghst)

 # ghs_values, son valores que estan en una familia ocupando misma fila o columna, haciendo que ese valor si o si vaya ahi


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
