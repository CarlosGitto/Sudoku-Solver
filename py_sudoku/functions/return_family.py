"""Functions that return a family letter"""


def func_abc(dictionary: dict, i: int, j: int) -> str:
    """Take a dict and two ints and return the letter of the family"""
    x = str(i)+str(j)
    for name, val in dictionary.items():
        if x in name:
            return(name[0])
