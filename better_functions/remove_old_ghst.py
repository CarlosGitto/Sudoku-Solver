import numpy as np


def remove_old_ghst(ghst_dict: dict, my_dict: dict, key: int):
    if type(my_dict[key]) == int or type(my_dict[key]) == np.int64:
        try:
            ghst_dict.pop(key)
        except KeyError:
            pass
    else:
        print("try to remove key not solved from ghst", key, my_dict[key])
