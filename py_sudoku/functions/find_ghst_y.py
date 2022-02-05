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
