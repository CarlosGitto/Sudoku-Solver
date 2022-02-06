# Adueña de una fila a un valor
def remove_ghst_values(sudoku_line: list, dict: dict, pointer: int, lst_ghst: list, family: str, row_type: bool):

    for index, value in enumerate(sudoku_line):
        if row_type:
            numbers = str(pointer)+str(index)
        numbers = str(index)+str(pointer)
        if value == 0:
            for name in dict.keys():
                if numbers in name and type(dict[name]) == list and len(dict[name]) > 1 and family not in name:
                    for ghst in lst_ghst:
                        if ghst in dict[name]:
                            print(ghst, "es un ghst y fue removido de", name)
                            dict[name].remove(ghst)
                            print(name, dict[name])
