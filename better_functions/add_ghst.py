def add_ghst(ghst_dict: dict, key: str, value: int):
    if key in ghst_dict.keys():
        if value not in ghst_dict[key]:
            ghst_dict[key].append(value)
    else:
        ghst_dict[key] = [value]
