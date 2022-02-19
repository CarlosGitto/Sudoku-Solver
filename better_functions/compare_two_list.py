def compare_list(list_1: list, list_2: list) -> list:
    repeated_items = []
    for index_1, item_1 in enumerate(list_1):
        for index_2, item_2 in enumerate(list_2):
            if item_1 == item_2 and index_1 != index_2:
                if item_1 not in repeated_items:
                    repeated_items.append(item_1)
    return repeated_items
