"""Functions that return a family letter"""


def return_list_of_family(my_dict: dict, key: str) -> list:
    """Take a dict and two ints and return the letter of the family"""
    family = [k for k in my_dict.keys() if key[0] in k]
    return family


def return_family_key(key: str) -> str:
    return key[0]
