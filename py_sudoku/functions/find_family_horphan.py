from py_sudoku.constantes import kn_lst_3

# Encuentra valores no repetidos para una lista que viene  de la familia


def count_last_chk(lst):
    for i in lst:
        count = 0
        for j in range(len(lst)):
            if i == lst[j]:
                count += 1
        if count == 1:
            return(i)

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
