import requests
import json
import random
import numpy as np

"""

files=dict(foo='bar')
"""


def check_difficult(level: int) -> str:
    my_dict = {
        "60": "muy_facil",
        "20": "facil",
        "14": "normal",
        "10": "dificil",
        "-20": "muy dificil"
    }
    return my_dict[level]


def make_a_save(sudoku_info):
    with open("sudoku.json", "w") as file:
        file.write(json.dumps(sudoku_info, indent=2))


def get_sudoku() -> tuple:
    """
    Make a get request that brings a random sudoku from database
    """

    random_sudoku = "".join([str(random.randint(0, 9)) for k in range(13)])

    resb = requests.get(
        f"https://www.sudoku-online.org/getsudoku.php?{random_sudoku}", files=dict(nivel=14))

    sudoku = json.loads(resb.content.decode('utf-8'))

    initial_sudoku = sudoku["sudoku"].replace(".", "0")
    difficulty = check_difficult(sudoku["nivel"])
    sudoku_solved = sudoku["solucion"]
    # make_a_save(sudoku)

    return initial_sudoku, sudoku_solved, difficulty


def make_a_sudoku():
    """
    Transform a sudoku string into a matrix 9x9
    and return it
    """

    initial_sudoku, solution, difficulty = get_sudoku()

    sudokus = [initial_sudoku, solution]
    my_sudokus = []
    for i, sudoku in enumerate(sudokus):
        final_sudoku = []
        x = len(sudoku)
        n = 9
        for index in range(0, x, n):
            final_sudoku.append(list(sudoku[index: index + n]))

        for i, sub_list in enumerate(final_sudoku):
            final_sudoku[i] = [int(k) for k in sub_list]

        my_sudokus.append(np.array(final_sudoku))

    return my_sudokus[0], my_sudokus[1], difficulty
