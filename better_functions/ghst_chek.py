
def can_be_added(ghst_dict: dict, value: int, key: str):
    """
    This function decide if an elemnt can be assign to a key 
    if the value isnt a ghst
    """
    if key not in ghst_dict.keys():
        return True
    else:
        if value in ghst_dict[key]:
            return False
        else:
            return True
