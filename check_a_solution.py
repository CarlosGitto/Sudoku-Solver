from get_sudoku import make_a_sudoku
from main import solver

def insert_values():
    solution_string = input("String of Solution :")
    my_sudoku_solution = make_a_sudoku(solution_string)
    solver(my_sudoku=my_sudoku_solution)

if __name__ == "__main__":
    insert_values()

        