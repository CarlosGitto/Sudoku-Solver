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
