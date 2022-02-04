from textwrap import indent
import requests
import io
import json
import random
import numpy as np


def make_a_save(sudoku_info):
    with open("sudoku.json", "w") as file:
        file.write(json.dumps(sudoku_info, indent=2))


def get_sudoku():
    """
    Make a get request that brings a random sudoku from database
    """

    random_sudoku = "".join([str(random.randint(0, 9)) for k in range(13)])

    resb = requests.get(
        f"https://www.sudoku-online.org/getsudoku.php?{random_sudoku}")

    sudoku = json.loads(resb.content.decode('utf-8'))

    initial_sudoku = sudoku["sudoku"].replace(".", "0")

    make_a_save(sudoku)

    return initial_sudoku


def make_a_sudoku():
    """
    Transform a sudoku string into a matrix 9x9
    and return it
    """

    initial_sudoku = get_sudoku()
    final_sudoku = []
    x = len(initial_sudoku)
    n = 9
    for index in range(0, x, n):
        final_sudoku.append(list(initial_sudoku[index: index + n]))

    for i, sub_list in enumerate(final_sudoku):
        final_sudoku[i] = [int(k) for k in sub_list]

    my_sudoku = np.array(final_sudoku)

    return my_sudoku
